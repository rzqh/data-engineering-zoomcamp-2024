variable "project" {
  description = "Project"
  default     = "rzqh-data-engineering-zoomcamp" #id project
}

variable "region" {
  description = "Region"
  default     = "asia-southeast2"
}

variable "location" {
  description = "Project location"
  default     = "asia-southeast2"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "dezoomcamp_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "rzqh-de-zoomcamp-bucket"
}

variable "gcs_storage_class" {
  description = "My Storage Class Name"
  default     = "STANDARD"
}

variable "credentials" {
    description = "My Credentials"
    default = "./keys/my-creds.json"
}