app = "anonxmusic-ypgy9w"   # اسم التطبيق عندك على Fly.io
primary_region = "cdg"       # أقرب سيرفر ليك أو سيرفر رئيسي

[build]
  dockerfile = "Dockerfile"

[http_service]
  auto_start_machines = true
  auto_stop_machines = false   # منع توقف البوت تلقائيًا
  force_https = true
  internal_port = 8080         # البورت الصحيح
  min_machines_running = 1     # دايمًا ماكينة شغالة
  processes = ["app"]

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory = "1gb"
