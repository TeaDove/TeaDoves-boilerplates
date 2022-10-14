terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

resource "yandex_message_queue" "queue" {
  name                       = join("-", [var.name_prefix, "queue"])
  visibility_timeout_seconds = 600
  receive_wait_time_seconds  = 0
  message_retention_seconds  = 1209600

  access_key = yandex_iam_service_account_static_access_key.sa_static_key.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa_static_key.secret_key
}


resource "yandex_iam_service_account" "sa" {
  name = join("-", [var.name_prefix, "message-queue-sa"])
}

resource "yandex_resourcemanager_folder_iam_binding" "sa_binding" {
  role      = each.value
  members   = ["serviceAccount:${yandex_iam_service_account.sa.id}"]
  folder_id = var.yc_folder_id
  for_each = {
    "role1" : "editor"
  }
}

resource "yandex_iam_service_account_static_access_key" "sa_static_key" {
  service_account_id = yandex_iam_service_account.sa.id
}
