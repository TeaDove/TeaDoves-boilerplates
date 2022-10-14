terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

resource "yandex_vpc_network" "main_vpc" {
  name = join("-", [var.name_prefix, "vpc-network"])
}

resource "yandex_vpc_subnet" "main_subnet" {
  v4_cidr_blocks = ["10.2.0.0/16"]
  network_id     = yandex_vpc_network.main_vpc.id
}
