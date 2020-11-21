resource "tls_private_key" "private_key" {
  algorithm   = "ECDSA"
  ecdsa_curve = "P384"

  # Store the certificate's private key in a file.
  provisioner "local-exec" {
    command = "echo '${tls_private_key.private_key.private_key_pem}' > '/tmp/tls/tf_private_key.pem' && chmod 075 /tmp/tls/tf_private_key.pem'"
  }
}

output "private_key" {
    value = tls_private_key.private_key
}

resource "tls_self_signed_cert" "server_selfsigned_cert" {
  key_algorithm   = "ECDSA"
  private_key_pem = tls_private_key.private_key.private_key_pem

  subject {
    common_name  = "example.com"
    organization = "ACME Examples, Inc"
  }

  validity_period_hours = 12

  allowed_uses = [
    "key_encipherment",
    "digital_signature",
    "server_auth",
  ]
}

output "selfsigned_cert" {
    value = tls_self_signed_cert.server_selfsigned_cert
}

resource "tls_cert_request" "example" {
  key_algorithm = "ECDSA"
  private_key_pem = tls_private_key.private_key.private_key_pem

  subject {
    common_name = "acme.com"
    organization = "Acme Industrials, Inc"
  }
}

output "cert_request" {
    value = tls_cert_request.example
}
