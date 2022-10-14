variable "db_dsn" { sensitive = true }
variable "show_swagger" {}
variable "yc_folder_id" {}
variable "is_prod" {
  type = bool
}
variable "log_level" {}
variable "name_prefix" {}
variable "terraform_dir_path" {}
