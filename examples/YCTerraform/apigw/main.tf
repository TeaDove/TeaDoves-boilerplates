terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

resource "yandex_api_gateway" "rest_api" {
  name = lower(replace(join("_", [var.global_deployment_settings["name_prefix"], "APIGW"]), "_", "-"))
  spec = <<-EOT
openapi: 3.0.0
info:
  title: Sample API
  version: 1.0.0
paths:
  /{proxy+}:
    x-yc-apigateway-any-method:
      x-yc-apigateway-integration:
        type: cloud_functions
        function_id: ${var.function_id}
        service_account_id: ${var.function_service_account_id}
        payload_format_version: "1.0"
      parameters:
      - name: proxy
        in: path
        required: false
        schema:
          type: string
EOT
}
