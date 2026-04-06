# 1. This creates the GCS Bucket (if it doesn't exist)
resource "google_storage_bucket" "landing_zone" {
  name          = "yalluri-raw-landing-zone-prod" 
  location      = "US"
  force_destroy = true # Allows Terraform to delete it later if needed
}

# 2. This creates the Service Account for Databricks to use
resource "google_service_account" "databricks_sa" {
  account_id   = "databricks-uc-sa"
  display_name = "Databricks Unity Catalog Service Account"
}