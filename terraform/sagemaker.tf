resource "aws_sagemaker_notebook_instance" "ni" {
  name          = "my-notebook-instance"
  role_arn      = aws_iam_role.test_role.arn
  instance_type = "ml.t2.medium"
  root_access = "Disabled"
  subnet_id = aws_subnet.pike.id
  # Noncompliant: SageMaker Notebook is not encrypted at rest using KMS CMK.
  tags = {
    Name = "foo"
  }
}
