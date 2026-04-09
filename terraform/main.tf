# 1. Creating Storage Bucket
resource "google_storage_bucket" "landing_zone" {
  name          = "yalluri-raw-landing-zone-prod" 
  location      = "US"
  force_destroy = true # Allows Terraform to delete it later if needed
}

# 2. Creating the Servic Accounte
resource "google_service_account" "databricks_sa" {
  account_id   = "databricks-uc-sa"
  display_name = "Databricks Unity Catalog Service Account"
}

# 1. Creating the Secret "Container" in GCP
resource "google_secret_manager_secret" "landing_zone_path" {
  secret_id = "landing-zone-path"
  replication {
    auto {}
  }
}

# 2. Adding the path
resource "google_secret_manager_secret_version" "path_version" {
  secret      = google_secret_manager_secret.landing_zone_path.id
  secret_data = "gs://yalluri-raw-landing-zone/weatherAUS.csv"
}

resource "google_storage_bucket_iam_member" "databricks_access" {
  bucket = "yalluri-raw-landing-zone"
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.databricks_sa.email}"
}
