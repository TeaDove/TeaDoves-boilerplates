variable "db_dsn" { sensitive = true }
variable "show_swagger" {}
variable "log_level" {}

variable "global_deployment_settings" { type = map(string) }
