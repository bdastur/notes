resource "aws_lambda_layer_version" "lambda_layer" {
    filename = "tempdir/py38_layer.zip"
    layer_name = "py38_layer"
    
    compatible_runtimes = ["python3.8"]
}
