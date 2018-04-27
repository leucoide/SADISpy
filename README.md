# SADISpy
SADISpy is simple Python script to ease the batch ingest of he Brazilian ANCINE's SADIS XML for Movie theater releases in Brazil.   
   
* Current works with the 1.2 Version of the SADIS detailed XML.   
* It is Open Source Software, available as is, with no Support provided for free. Contact gus@tesserato.video to request paid assistance.   
   
XML Format:   
   
![Image of xml format](https://raw.githubusercontent.com/gustavohmsilva/SADISpy/master/doc/xml_format_flux1.2.png)   
      
* [Documentation](https://raw.githubusercontent.com/gustavohmsilva/SADISpy/master/doc/detailed_xml_sadis1.2.pdf)   
* [Working XML example 1.2](https://raw.githubusercontent.com/gustavohmsilva/SADISpy/master/doc/valid_xml_example1.2.xml)


## Usage:
1. Learn to you the terminal on your Linux or MacOSX PC
2. $sadis.py -distribuidor /PATH/TO/CSVDISTRIBUIDOR.CSV 
3. $sadis.py -cinema /PATH/TO/CSVCINEMAINFO.CSV 
3. $sadis.py -sessoes /PATH/TO/CSVSESSOESDECINEMA.CSV 
