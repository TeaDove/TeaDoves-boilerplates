terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


module "lambda_api" {
  source = "./lambda_api"

  yc_folder_id       = var.yc_folder_id
  is_prod            = var.is_prod
  log_level          = var.log_level
  name_prefix        = var.name_prefix
  terraform_dir_path = var.terraform_dir_path

  show_swagger     = var.show_swagger
  db_dsn           = var.db_dsn
}

module "apigw" {
  source = "./apigw"

  function_id                 = module.lambda_api.function_id
  function_service_account_id = module.lambda_api.service_account_id
  name_prefix                 = var.name_prefix
}

module "sqs" {
  source = "./sqs"

  name_prefix  = var.name_prefix
  yc_folder_id = var.yc_folder_id
}
