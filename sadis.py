#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import csv
import os


def writeDadosEnvio(NomeArquivo,remetenteCNPJ,remetenteRazaoSocial,distribuidoraCNPJ,distribuidoraCdRegAncine,distribuidoraRazaoSocial,dataInicio,dataFim):
    dadosRetorno = '<?xml version="1.0" encoding="utf-8"?>\n'
    dadosRetorno = dadosRetorno + '<XSD_SADIS xmlns:tns="http://www.example.org/tipos/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://ancinet/media/SAVISADIS/xsd/Schema_XML_SADIS_v1_2.xsd" version="1.2">\n'
    if not NomeArquivo == '': dadosRetorno = dadosRetorno + '<dadosEnvio>\n\t<nomeArquivo>' + str(NomeArquivo) + '</nomeArquivo>\n'
    if not remetenteCNPJ == '': dadosRetorno = dadosRetorno + '\t<empresaRemetente>\n\t\t<CNPJ>' + str(remetenteCNPJ) + '</CNPJ>\n'
    if not remetenteRazaoSocial == '': dadosRetorno = dadosRetorno + '\t\t<razaoSocial>' + str(remetenteRazaoSocial) + '</razaoSocial>\n\t</empresaRemetente>\n'
    if not distribuidoraCNPJ == '': dadosRetorno = dadosRetorno + '\t<empresaDistribuidora>\n\t\t<CNPJ>' + str(distribuidoraCNPJ) + '</CNPJ>\n'
    if not distribuidoraCdRegAncine == '': dadosRetorno = dadosRetorno + '\t\t<cdRegAncine>' + str(distribuidoraCdRegAncine) + '</cdRegAncine>\n'
    if not distribuidoraRazaoSocial == '': dadosRetorno = dadosRetorno + '\t\t<razaoSocial>' + str(distribuidoraRazaoSocial) + '</razaoSocial>\n\t</empresaDistribuidora>\n'
    if not dataInicio == '': dadosRetorno = dadosRetorno + '\t<periodoInformado>\n\t\t<dataInicio>' + str(dataInicio) + '</dataInicio>\n'
    if not dataFim == '': dadosRetorno = dadosRetorno + '\t\t<dataFim>' + str(dataFim) + '</dataFim>\n\t</periodoInformado>\n</dadosEnvio>\n'
    return dadosRetorno

def writeDadosExibicao(cdRegAncineObra,tituloObra,dataLancamento):
    if not cdRegAncineObra == '': dadosRetorno = '<dadosExibicao>\n\t<obra>\n\t\t<cdRegAncine>' + str(cdRegAncineObra) + '</cdRegAncine>\n'
    if not tituloObra == '': dadosRetorno = dadosRetorno + '\t\t<tituloOriginal>' + str(tituloObra) + '</tituloOriginal>\n'
    if not dataLancamento == '': dadosRetorno = dadosRetorno + '\t\t<dataLancamento>' + str(dataLancamento) + '</dataLancamento>\n\t\t<salas>\n'
    return dadosRetorno

def writeDadosCinema(cdRegAncineSala,CNPJSala,nomeSala,ufSala,municipioSala,cdRegAncineComplexo):
    if not cdRegAncineSala == '': dadosRetorno = '\t\t\t<sala>\n\t\t\t\t<cdRegAncineSala>' + str(cdRegAncineSala) + '</cdRegAncineSala>\n'
    if not CNPJSala == '': dadosRetorno = dadosRetorno + '\t\t\t\t<CNPJSala>' + str(CNPJSala) + '</CNPJSala>\n'
    if not nomeSala == '': dadosRetorno = dadosRetorno + '\t\t\t\t<nomeSala>' + str(nomeSala) + '</nomeSala>\n'
    if not ufSala == '': dadosRetorno = dadosRetorno + '\t\t\t\t<ufSala>' + str(ufSala) + '</ufSala>\n'
    if not municipioSala == '': dadosRetorno = dadosRetorno + '\t\t\t\t<municipioSala>' + str(municipioSala) + '</municipioSala>\n'
    if not cdRegAncineComplexo == '': dadosRetorno = dadosRetorno + '\t\t\t\t<cdRegAncineComplexo>' + str(cdRegAncineComplexo) + '</cdRegAncineComplexo>\n'
    dadosRetorno = dadosRetorno + '\t\t\t\t<exibicoes>\n\t\t\t\t\t<detalheExibicao>\n'
    return dadosRetorno
outputXML = ''
# ABA 1 DA PLANILHA
if sys.argv[1] == '-distribuidor':
    arquivoCsv = str(sys.argv[2])
    os.system('sed 1,1d ' + arquivoCsv + ' >> temp.csv && mv teste.csv ' + arquivoCsv + '')
    f = open(arquivoCsv)
    csv_f = csv.reader(f)
    for row in csv_f:
        outputXML = writeDadosEnvio(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        outputXML = outputXML + writeDadosExibicao(row[8],row[9],row[10])
    f.close()
    f = open("parcial_sadis.xml", "w")
    f.write(outputXML)
    f.close()
elif sys.argv[1] == '-cinema':
    arquivoCsv = str(sys.argv[2])
    os.system('sed 1,1d ' + arquivoCsv + ' >> temp.csv && mv teste2.csv ' + arquivoCsv + '')
    f = open(arquivoCsv)
    csv_f = csv.reader(f)
    for row in csv_f:
        outputXML + writeDadosCinema(row[0],row[1],row[2],row[3],row[4],row[5])
    f.close()
    os.system('mv parcial_sadis.xml parcial_sadis-exib.xml')
    f = open("parcial_sadis-exib.xml", "w")
    f.write(outputXML)
    f.close()
else:
    print('Erro! Use os argumentos -distribuidor ou -cinema seguidos do arquivo csv desejado')
