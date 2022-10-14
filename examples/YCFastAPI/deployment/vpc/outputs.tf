output "vpc_network_id" {
  value = yandex_vpc_network.main_vpc.id
}

output "vpc_subnet_id" {
  value = yandex_vpc_subnet.main_subnet.id
}
