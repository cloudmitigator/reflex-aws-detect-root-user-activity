provider "aws" {
  region = "us-east-1"
}

module "detect_root_user_activity" {
  source           = "git@github.com:cloudmitigator/reflex.git//modules/cwe_sns_email?ref=v0.0.1"
  rule_name        = "DetectRootUserActivity"
  rule_description = "Rule to check when the root user performs any actions"

  event_pattern = <<PATTERN
{
  "detail-type": [
    "AWS API Call via CloudTrail",
    "AWS Console Sign In via CloudTrail"
  ],
  "detail": {
    "userIdentity": {
      "type": ["Root"]
    }
  }
}
PATTERN

  topic_name = "DetectRootUserActivity"
  target_id  = "DetectRootUserActivity"
  email      = var.email
}
