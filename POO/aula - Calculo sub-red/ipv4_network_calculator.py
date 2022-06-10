import re

class Ipv4NetworkCalculator():
  def __init__(self, ip='', prefixo="", mascara="", rede="", broadcast="", numero_ips=""):
    self.ip = ip
    self.prefixo = prefixo
    self.mascara = mascara
    self.rede = rede
    self.broadcast = broadcast
    self.numero_ips = numero_ips

    if self.ip == "":
      raise ValueError("IP nao enviado.")

    self.ip_tem_prefixo()

    print(self.ip, self.prefixo)


  def ip_tem_prefixo(self):
    ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,2}$')

    if not ip_prefixo_regexp.search(self.ip):
      return

    divide_ip = self.ip.split("/")
    self.ip = divide_ip[0]
    self.prefixo = divide_ip[1]


if __name__ == "__main__":
  ipv4 = Ipv4NetworkCalculator(ip="192.168.0.1/24")


