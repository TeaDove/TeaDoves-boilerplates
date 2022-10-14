terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

locals {
  lambda_name     = "api-entrypoint"
  src_directory   = "${var.terraform_dir_path}/../backend"
  lambda_fullname = join("-", [var.name_prefix, local.lambda_name])
}


data "archive_file" "archive" {
  type        = "zip"
  source_dir  = local.src_directory
  output_path = "${local.src_directory}/.deploy.zip"
  excludes    = ["${local.src_directory}/.deploy.zip"]
}

resource "yandex_function" "function" {
  name               = local.lambda_fullname
  user_hash          = data.archive_file.archive.output_base64sha256
  runtime            = "python39"
  entrypoint         = "entrypoints.yc_lambda_handler"
  memory             = "128"
  execution_timeout  = "30"
  service_account_id = yandex_iam_service_account.sa.id

  content {
    zip_filename = data.archive_file.archive.output_path
  }

  environment = {
    LOG_LEVEL               = var.log_level
    POWERTOOLS_SERVICE_NAME = local.lambda_fullname

    db_dsn           = var.db_dsn
    show_swagger     = var.show_swagger

    security_yc_access_key = yandex_iam_service_account_static_access_key.sa_static_key.access_key
    security_yc_secret_key = yandex_iam_service_account_static_access_key.sa_static_key.secret_key
  }
}

resource "yandex_iam_service_account" "sa" {
  name = join("-", [var.name_prefix, "sa"])
}

resource "yandex_resourcemanager_folder_iam_binding" "sa_binding" {
  role      = each.value
  members   = ["serviceAccount:${yandex_iam_service_account.sa.id}"]
  folder_id = var.yc_folder_id
  for_each = {
    "role1" : "serverless.functions.invoker"
    "role2" : "serverless.containers.invoker"
    "role3" : "editor"
  }
}

resource "yandex_iam_service_account_static_access_key" "sa_static_key" {
  service_account_id = yandex_iam_service_account.sa.id
}
