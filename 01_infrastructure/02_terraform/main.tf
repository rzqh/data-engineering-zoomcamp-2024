# sumber: dokomentasi terraform https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs

terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.14.0"
    }
  }
}

provider "google" {
    credentials = var.credentials
    project = var.project #id project
    region = var.region
}

resource "google_storage_bucket" "auto-expire"{
    name = var.gcs_bucket_name
    location = var.location
    
    #Optional, but recommended settings:
    storage_class = var.gcs_storage_class
    uniform_bucket_level_access = true

    versioning {
        enabled = true
    }

    lifecycle_rule {      
      action {
        type = "Delete"
      }
      condition {
        age = 30 // hari
      }
    }

    force_destroy = true
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
}