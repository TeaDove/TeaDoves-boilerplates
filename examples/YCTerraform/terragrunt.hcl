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
  src_path =  "${local.terraform_dir_path}/${local.local_yaml_config["src_path"]}"
  name_prefix        = lower(join("-", [title(local.stage), title(local.department), local.stack]))
  global_deployment_settings = {
       "stage" : local.stage
       "department" : local.department
       "stack" : local.stack
       "is_prod" : local.is_prod
       "terraform_dir_path" : local.terraform_dir_path
       "src_path": local.src_path
       "name_prefix" : local.name_prefix
       "yc_cloud_id"  : local.stage_vars["yc_cloud_id"]
       "yc_folder_id" : local.stage_vars["yc_folder_id"]
       "yc_zone"      : local.stage_vars["yc_zone"]
     }
}

inputs = merge(local.stage_vars, { global_deployment_settings = local.global_deployment_settings }
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
