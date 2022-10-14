terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

data "yandex_compute_image" "container-optimized-image" {
  family = "container-optimized-image"
}

resource "yandex_compute_instance" "db_server" {
  name        = join("-", [var.name_prefix, "db-server"])
  platform_id = "standard-v2"

  resources {
    cores         = 2
    memory        = 0.5
    core_fraction = 5
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.container-optimized-image.id
    }
  }

  network_interface {
    ip_address = var.internal_ip_address
    subnet_id  = var.vpc_subnet_id
    nat        = true
  }

  metadata = {
    docker-compose = templatefile("${var.terraform_dir_path}/cc/docker-compose.tftpl",
      { container_image_url = var.container_image_url,
        postgres_user       = var.postgres_user
    postgres_password = var.postgres_password })
    user-data = file("${var.terraform_dir_path}/cc/user-data.yml")
  }
  service_account_id = yandex_iam_service_account.sa.id

  scheduling_policy {
    preemptible = true
  }
}

resource "yandex_iam_service_account" "sa" {
  name = join("-", [var.name_prefix, "sa"])
}

resource "yandex_resourcemanager_folder_iam_binding" "sa_binding" {
  role      = each.value
  members   = ["serviceAccount:${yandex_iam_service_account.sa.id}"]
  folder_id = var.yc_folder_id
  for_each = {
    "role1" : "container-registry.images.puller"
  }
}
