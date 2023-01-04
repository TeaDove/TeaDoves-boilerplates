variable "container_image_url" {}
variable "postgres_user" {}
variable "postgres_password" {}
variable "internal_ip_address" {}
variable "vpc_subnet_id" {}

variable "global_deployment_settings" { type = map(string) }