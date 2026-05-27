# AutoClicker

Um auto-clicker simples para Linux utilizando a biblioteca `evdev` e `uinput`.

## Dependências

### Sistema
- Linux
- Acesso ao `/dev/uinput` (geralmente requer permissões de grupo `uinput` ou `root`).
- Python 3.x

### Python
As dependências Python podem ser instaladas via `pip`:

```bash
pip install evdev
```

## Configuração de Permissões (UInput)

Para executar o script sem `sudo`, seu usuário precisa de permissões para acessar o `/dev/uinput`.

1. Crie uma regra udev:
   ```bash
   echo 'KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/99-uinput.rules
   ```
2. Crie o grupo `uinput` (se não existir) e adicione seu usuário:
   ```bash
   sudo groupadd uinput
   sudo usermod -aG uinput $USER
   ```
3. Recarregue as regras ou reinicie:
   ```bash
   sudo udevadm control --reload-rules && sudo udevadm trigger
   ```
   *Nota: Pode ser necessário fazer logout e login novamente para as alterações de grupo surtirem efeito.*

## Como Usar

Execute o script `start.py`:

```bash
python start.py [opções]
```

### Opções
- `--ms`: Intervalo entre cliques em milissegundos (padrão: `50`).
- `--button`: Botão para clicar (`left` ou `right`, padrão: `left`).
- `--mode`: Modo de operação (`hold` ou `toggle`, padrão: `hold`).

### Exemplos

1. **Clique esquerdo a cada 100ms no modo toggle:**
   ```bash
   python start.py --ms 100 --mode toggle
   ```
   *Pressione ENTER no terminal para ligar/desligar.*

2. **Clique direito rápido (10ms) no modo hold:**
   ```bash
   python start.py --ms 10 --button right --mode hold
   ```
   *Pressione ENTER no terminal para simular o segurar do botão.*

## Tecla de Ação

Atualmente, o script utiliza a tecla **ENTER** dentro do terminal onde está sendo executado para controlar o estado do clique:

- **Modo Toggle:** Pressione ENTER uma vez para ligar e ENTER novamente para desligar.
- **Modo Hold:** Pressione ENTER para alternar entre "segurar" e "soltar" o clique virtual.

### Nota sobre Teclas de Atalho (Hotkeys)
A versão atual não captura teclas globais do sistema (ex: F1, F6). Se você desejar mudar o comportamento para responder a uma tecla específica do teclado em vez do ENTER no terminal, seria necessário integrar uma biblioteca como `pynput` ou ler eventos diretamente de `/dev/input/`.

## Funcionamento
O script cria um dispositivo de entrada virtual chamado "auto-clicker" via `uinput`. Ele utiliza uma thread separada para gerenciar o loop de cliques, garantindo precisão no timing.
