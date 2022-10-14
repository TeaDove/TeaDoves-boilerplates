### DO NOT CHANGE ###
locals {
  stage = get_env("STAGE", "stable")

  # В deploy_config.yaml хранятся настройки для конкретного стека, они овверайдят дефолтные настройки
  local_yaml_config  = yamldecode(file("deploy_config.yaml"))
  local_stage_config = lookup(local.local_yaml_config["envs"], local.stage, {})
  local_defaults     = lookup(local.local_yaml_config, "defaults", {})
  # Соединяем local, default и common конфиги по приоритету локальности Default -> LocalDefault -> Local.
  stage_vars = merge(local.local_defaults, local.local_stage_config)

  department         = local.local_yaml_config["department"]
  stack              = local.local_yaml_config["stack"]
  is_prod            = lookup(local.stage_vars, "is_prod", local.stage == "prod" ? true : false)
  terraform_dir_path = get_env("PWD", ".")
  name_prefix        = lower(join("-", [title(local.stage), title(local.department), local.stack]))
}

inputs = merge(local.stage_vars, {
  stage      = local.stage
  stack      = local.stack
  department = local.department

  terraform_dir_path = local.terraform_dir_path
  is_prod            = local.stage == "prod" ? true : false
  name_prefix        = local.name_prefix
  }
)

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
provider "yandex" {
  cloud_id  = "${local.stage_vars["yc_cloud_id"]}"
  folder_id = "${local.stage_vars["yc_folder_id"]}"
  zone      = "${local.stage_vars["yc_zone"]}"
}
EOF
}
### DO NOT CHANGE ###
