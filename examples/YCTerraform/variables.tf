variable "db_dsn" { sensitive = true }
variable "show_swagger" {}
variable "log_level" {}
variable "vpc_ip_blocks" { type = list(string) }
variable "cc_ip_addresses" { type = list(string) }

### DO NOT CHANGE ###
variable "global_deployment_settings" { type = map(string) }
### DO NOT CHANGE ###
