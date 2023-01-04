terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

resource "yandex_vpc_network" "main_vpc" {
  name = join("-", [var.global_deployment_settings["name_prefix"], "vpc-network"])
}

resource "yandex_vpc_subnet" "main_subnet" {
  v4_cidr_blocks = var.vpc_ip_blocks
  network_id     = yandex_vpc_network.main_vpc.id
}
