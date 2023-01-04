terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


module "lambda_api" {
  source = "./lambda_api"

  log_level    = var.log_level
  show_swagger = var.show_swagger
  db_dsn       = var.db_dsn

  global_deployment_settings = var.global_deployment_settings
}

module "apigw" {
  source = "./apigw"

  function_id                 = module.lambda_api.function_id
  function_service_account_id = module.lambda_api.service_account_id

  global_deployment_settings = var.global_deployment_settings
}

module "sqs" {
  source = "./sqs"

  global_deployment_settings = var.global_deployment_settings
}

module "vpc" {
  source = "./vpc"

  vpc_ip_blocks = var.vpc_ip_blocks

  global_deployment_settings = var.global_deployment_settings
}

# module "cc" {
#   source = "./cc"

#   global_deployment_settings = var.global_deployment_settings
# }
