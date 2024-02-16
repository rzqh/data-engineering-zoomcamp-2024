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
    credentials = "./keys/my-creds.json"
    project = "rzqh-data-engineering-zoomcamp" #id project
    region = "asia-southeast2"
}

resource "google_storage_bucket" "auto-expire"{
    name = "rzqh-de-zoomcamp-bucket"
    location = "asia-southeast2"
    
    #Optional, but recommended settings:
    storage_class = "STANDARD"
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