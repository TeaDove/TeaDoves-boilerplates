output "apigw_invoke_url" {
  value = "https://${module.apigw.apigw_id}.apigw.yandexcloud.net"
}
output "queue_url" {
  value = module.sqs.queue_url
}
