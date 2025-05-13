# Caminho local do projeto
$localPath = "C:\Users\Liandro\Documents\Github\deepstart"

# Usuário e IP do servidor
$user = "lbulegon"
$serverIp = "192.168.0.69"

# Caminho de destino no servidor
$remotePath = "~/deepstart"

Write-Host "Iniciando envio do projeto para $user@$serverIp:$remotePath`n"

scp -r "$localPath" "$user@$serverIp:$remotePath"

if ($?) {
    Write-Host "`n✅ Projeto enviado com sucesso!"
} else {
    Write-Host "`n❌ Erro no envio do projeto."
}
