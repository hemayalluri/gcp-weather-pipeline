terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    databricks = {
      source = "databricks/databricks"
    }
  }
}

provider "google" {
  project = "inspired-cortex-491503-i3" # Replace with your actual Project ID
  region  = "us-east1"
}