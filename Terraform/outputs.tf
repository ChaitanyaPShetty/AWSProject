output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnets" {
  value = aws_subnet.public[*].id
}

output "private_subnets" {
  value = aws_subnet.private[*].id
}

output "web_security_group" {
  value = aws_security_group.web_sg.id
}

output "rds_security_group" {
  value = aws_security_group.rds_sg.id
}
