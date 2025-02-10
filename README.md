Script em Python que monitora uma pasta de origem e copia automaticamente para o destino, nesse caso apenas os arquivos que contêm a palavra "parte" no nome. Usei esse parâmetro no nome do arquivo, pensando em uma solução para uma situação onde arquivos grandes 
são divididos em partes menores e precisam ser transferidos conforme são gerados. O funcionamento é simples: o código compara os arquivos na pasta de origem e na pasta de destino, copiando apenas aqueles que ainda não existem no destino. A cada 90 segundos, 
o processo é repetido, garantindo que os arquivos sejam sincronizados continuamente. Para utilizar, basta definir os caminhos da pasta de origem e destino no código e executar o script.
--> Deixei algumas partes do script comentado para melhor configuração em cada caso.

Terminal durante o meio do processo:
![terminal_sincronizador](https://github.com/user-attachments/assets/15dd5c6e-fa6a-42b6-b89a-18e2c9a942ca)
