#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File zone.py
# Date 2020-02-27 15:55
# Author Akio

import json
from bs4 import BeautifulSoup

html = '<tbody><tr> <td><strong>UTC-11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--midway">Pacific/Midway</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/um"><span class="flag-icon flag-icon-um ' \
       'mr-10"></span>United States Minor Outlying Islands</a></td> <td> </td> </tr> <tr> ' \
       '<td><strong>UTC-11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--niue">Pacific/Niue</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nu"><span class="flag-icon flag-icon-nu ' \
       'mr-10"></span>Niue</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4036284"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Alofi</a> </td> </tr> <tr> <td><strong>UTC-11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--pago_pago">Pacific/Pago_Pago</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/as"><span class="flag-icon flag-icon-as ' \
       'mr-10"></span>American Samoa</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5881576"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pago Pago</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5881192"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tāfuna</a>, <a href="https://www.zeitverschiebung.net/cn/city/5881165"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ta`ū</a>, <a href="https://www.zeitverschiebung.net/cn/city/5881150"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Taulaga</a> </td> </tr> <tr> <td><strong>UTC-10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--adak">America/Adak</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--honolulu">Pacific/Honolulu</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5856195"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Honolulu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5852275"><i class="fa fa-map-marker pr-5 pl-5"></i>Pearl ' \
       'City</a>, <a href="https://www.zeitverschiebung.net/cn/city/5855927"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hilo</a>, <a href="https://www.zeitverschiebung.net/cn/city/5847486"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kailua</a>, <a href="https://www.zeitverschiebung.net/cn/city/5854686"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Waipahu</a> </td> </tr> <tr> <td><strong>UTC-10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--rarotonga">Pacific/Rarotonga</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ck"><span class="flag-icon flag-icon-ck mr-10"></span>Cook ' \
       'Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4035715"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Avarua</a> </td> </tr> <tr> <td><strong>UTC-10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--tahiti">Pacific/Tahiti</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pf"><span class="flag-icon flag-icon-pf ' \
       'mr-10"></span>French Polynesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4034561"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Faaa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4033936"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Papeete</a>, <a href="https://www.zeitverschiebung.net/cn/city/4033779"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Punaauia</a>, <a href="https://www.zeitverschiebung.net/cn/city/4033838"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pirae</a>, <a href="https://www.zeitverschiebung.net/cn/city/4034307"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mahina</a> </td> </tr> <tr> <td><strong>UTC-9:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--marquesas">Pacific/Marquesas</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pf"><span class="flag-icon flag-icon-pf ' \
       'mr-10"></span>French Polynesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/8063344"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Taiohae</a> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--anchorage">America/Anchorage</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5879400"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Anchorage</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5861897"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Fairbanks</a>, <a href="https://www.zeitverschiebung.net/cn/city/5861187"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Eagle River</a>, <a href="https://www.zeitverschiebung.net/cn/city/5879898"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Badger</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7262897"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Knik-Fairview</a> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--juneau">America/Juneau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5554072"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Juneau</a> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--metlakatla">America/Metlakatla</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--nome">America/Nome</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--sitka">America/Sitka</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5557293"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sitka</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5554428"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ketchikan</a> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--yakutat">America/Yakutat</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--gambier">Pacific/Gambier</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pf"><span class="flag-icon flag-icon-pf ' \
       'mr-10"></span>French Polynesia</a></td> <td> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--dawson">America/Dawson</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--los_angeles">America/Los_Angeles</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5368361"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Los Angeles</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5391811"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Diego</a>, <a href="https://www.zeitverschiebung.net/cn/city/5392171"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>San Jose</a>, <a href="https://www.zeitverschiebung.net/cn/city/5391959"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>San Francisco</a>, <a href="https://www.zeitverschiebung.net/cn/city/5809844"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Seattle</a> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--tijuana">America/Tijuana</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3981609"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tijuana</a>, <a href="https://www.zeitverschiebung.net/cn/city/3996069"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mexicali</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4006702"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ensenada</a>, <a href="https://www.zeitverschiebung.net/cn/city/3988392"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Rosarito</a>, <a href="https://www.zeitverschiebung.net/cn/city/3982266"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tecate</a> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--vancouver">America/Vancouver</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6173331"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vancouver</a>, <a href="https://www.zeitverschiebung.net/cn/city/6159905"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Surrey</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7281931"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Okanagan</a>, <a href="https://www.zeitverschiebung.net/cn/city/6174041"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Victoria</a>, <a href="https://www.zeitverschiebung.net/cn/city/5911606"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Burnaby</a> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--whitehorse">America/Whitehorse</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6180550"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Whitehorse</a> </td> </tr> <tr> <td><strong>UTC-8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--pitcairn">Pacific/Pitcairn</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pn"><span class="flag-icon flag-icon-pn ' \
       'mr-10"></span>Pitcairn</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4030723"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Adamstown</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--boise">America/Boise</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5586437"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Boise</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5601933"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nampa</a>, <a href="https://www.zeitverschiebung.net/cn/city/5600685"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Meridian</a>, <a href="https://www.zeitverschiebung.net/cn/city/5596475"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Idaho Falls</a>, <a href="https://www.zeitverschiebung.net/cn/city/5604045"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pocatello</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--cambridge_bay">America/Cambridge_Bay</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--chihuahua">America/Chihuahua</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4014338"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chihuahua</a>, <a href="https://www.zeitverschiebung.net/cn/city/4013720"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ciudad Delicias</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4004867"><i class="fa fa-map-marker pr-5 pl-5"></i>Hidalgo ' \
       'del Parral</a>, <a href="https://www.zeitverschiebung.net/cn/city/4012406"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Cuauhtémoc</a>, <a href="https://www.zeitverschiebung.net/cn/city/3994616"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nuevo Casas Grandes</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--creston">America/Creston</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--dawson_creek">America/Dawson_Creek</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5955960"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Fort St. John</a>, <a href="https://www.zeitverschiebung.net/cn/city/5935804"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dawson Creek</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--denver">America/Denver</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5520993"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>El Paso</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5419384"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Denver</a>, <a href="https://www.zeitverschiebung.net/cn/city/5454711"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Albuquerque</a>, <a href="https://www.zeitverschiebung.net/cn/city/5417598"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Colorado Springs</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5412347"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Aurora</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--edmonton">America/Edmonton</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5913490"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Calgary</a>, <a href="https://www.zeitverschiebung.net/cn/city/5946768"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Edmonton</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5955895"><i class="fa fa-map-marker pr-5 pl-5"></i>Fort ' \
       'McMurray</a>, <a href="https://www.zeitverschiebung.net/cn/city/6118158"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Red Deer</a>, <a href="https://www.zeitverschiebung.net/cn/city/6053154"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Lethbridge</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--fort_nelson">America/Fort_Nelson</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--hermosillo">America/Hermosillo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4004898"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hermosillo</a>, <a href="https://www.zeitverschiebung.net/cn/city/4013704"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ciudad Obregón</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4004886"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nogales</a>, <a href="https://www.zeitverschiebung.net/cn/city/3985604"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>San Luis Río Colorado</a>, <a href="https://www.zeitverschiebung.net/cn/city/3995019"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Navojoa</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--inuvik">America/Inuvik</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--mazatlan">America/Mazatlan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4012176"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Culiacán</a>, <a href="https://www.zeitverschiebung.net/cn/city/3996322"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mazatlán</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3981941"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tepic</a>, <a href="https://www.zeitverschiebung.net/cn/city/3997479"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Los Mochis</a>, <a href="https://www.zeitverschiebung.net/cn/city/4000900"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>La Paz</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--ojinaga">America/Ojinaga</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4013708"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ciudad Juárez</a>, <a href="https://www.zeitverschiebung.net/cn/city/8858105"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Manuel Ojinaga</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3994469"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ojinaga</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--phoenix">America/Phoenix</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5308655"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Phoenix</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5318313"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tucson</a>, <a href="https://www.zeitverschiebung.net/cn/city/5304391"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mesa</a>, <a href="https://www.zeitverschiebung.net/cn/city/5289282"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chandler</a>, <a href="https://www.zeitverschiebung.net/cn/city/5295985"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Glendale</a> </td> </tr> <tr> <td><strong>UTC-7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--yellowknife">America/Yellowknife</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6185377"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yellowknife</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--bahia_banderas">America/Bahia_Banderas</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4016734"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bucerías</a>, <a href="https://www.zeitverschiebung.net/cn/city/3980622"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Valle de Banderas</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--belize">America/Belize</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bz"><span class="flag-icon flag-icon-bz ' \
       'mr-10"></span>Belize</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3582677"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Belize City</a>, <a href="https://www.zeitverschiebung.net/cn/city/3581194"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Ignacio</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3581514"><i class="fa fa-map-marker pr-5 pl-5"></i>Orange ' \
       'Walk</a>, <a href="https://www.zeitverschiebung.net/cn/city/3582672"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Belmopan</a>, <a href="https://www.zeitverschiebung.net/cn/city/3582228"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Dangriga</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--chicago">America/Chicago</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4887398"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chicago</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4699066"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Houston</a>, <a href="https://www.zeitverschiebung.net/cn/city/4726206"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>San Antonio</a>, <a href="https://www.zeitverschiebung.net/cn/city/4684888"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dallas</a>, <a href="https://www.zeitverschiebung.net/cn/city/4671654"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Austin</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--costa_rica">America/Costa_Rica</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cr"><span class="flag-icon flag-icon-cr mr-10"></span>Costa ' \
       'Rica</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3621849"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>San José</a>, <a href="https://www.zeitverschiebung.net/cn/city/3622247"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Limón</a>, <a href="https://www.zeitverschiebung.net/cn/city/3621911"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Francisco</a>, <a href="https://www.zeitverschiebung.net/cn/city/3624955"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Alajuela</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3623076"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Liberia</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--el_salvador">America/El_Salvador</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sv"><span class="flag-icon flag-icon-sv mr-10"></span>El ' \
       'Salvador</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3583361"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>San Salvador</a>, <a href="https://www.zeitverschiebung.net/cn/city/3583096"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Soyapango</a>, <a href="https://www.zeitverschiebung.net/cn/city/3583334"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Santa Ana</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3583446"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Miguel</a>, <a href="https://www.zeitverschiebung.net/cn/city/3584399"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mejicanos</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--guatemala">America/Guatemala</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gt"><span class="flag-icon flag-icon-gt ' \
       'mr-10"></span>Guatemala</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3598132"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Guatemala City</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3592519"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mixco</a>, <a href="https://www.zeitverschiebung.net/cn/city/3587902"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Villa Nueva</a>, <a href="https://www.zeitverschiebung.net/cn/city/3591415"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Petapa</a>, <a href="https://www.zeitverschiebung.net/cn/city/3589885"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Juan Sacatepéquez</a> </td> </tr> <tr> ' \
       '<td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--knox">America/Indiana/Knox</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--tell_city">America/Indiana/Tell_City</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4265717"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tell City</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--managua">America/Managua</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ni"><span class="flag-icon flag-icon-ni ' \
       'mr-10"></span>Nicaragua</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3617763"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Managua</a>, <a href="https://www.zeitverschiebung.net/cn/city/3618030"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>León</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3617723"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Masaya</a>, <a href="https://www.zeitverschiebung.net/cn/city/3616035"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tipitapa</a>, <a href="https://www.zeitverschiebung.net/cn/city/3620381"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chinandega</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--matamoros">America/Matamoros</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3520339"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Reynosa</a>, <a href="https://www.zeitverschiebung.net/cn/city/3523466"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Heroica Matamoros</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3522551"><i class="fa fa-map-marker pr-5 pl-5"></i>Nuevo ' \
       'Laredo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3992619"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Piedras Negras</a>, <a href="https://www.zeitverschiebung.net/cn/city/4013728"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ciudad Acuña</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--menominee">America/Menominee</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5001669"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Menominee</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4997232"><i class="fa fa-map-marker pr-5 pl-5"></i>Iron ' \
       'Mountain</a>, <a href="https://www.zeitverschiebung.net/cn/city/4997249"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ironwood</a>, <a href="https://www.zeitverschiebung.net/cn/city/4998189"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kingsford</a>, <a href="https://www.zeitverschiebung.net/cn/city/4997238"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Iron River</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--merida">America/Merida</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3523349"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mérida</a>, <a href="https://www.zeitverschiebung.net/cn/city/3531732"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Campeche</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3530599"><i class="fa fa-map-marker pr-5 pl-5"></i>Ciudad ' \
       'del Carmen</a>, <a href="https://www.zeitverschiebung.net/cn/city/3526323"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kanasín</a>, <a href="https://www.zeitverschiebung.net/cn/city/3521108"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Progreso de Castro</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--mexico_city">America/Mexico_City</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3530597"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mexico City</a>, <a href="https://www.zeitverschiebung.net/cn/city/3526683"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Iztapalapa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3529612"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ecatepec</a>, <a href="https://www.zeitverschiebung.net/cn/city/4005539"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Guadalajara</a>, <a href="https://www.zeitverschiebung.net/cn/city/3521081"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Puebla</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--monterrey">America/Monterrey</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3482969"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gustavo A. Madero</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3995465"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Monterrey</a>, <a href="https://www.zeitverschiebung.net/cn/city/4005492"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Guadalupe</a>, <a href="https://www.zeitverschiebung.net/cn/city/3988086"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saltillo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3981254"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Torreon</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--north_dakota--beulah">America/North_Dakota/Beulah' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--north_dakota--center">America/North_Dakota/Center' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--north_dakota--new_salem">America/North_Dakota' \
       '/New_Salem</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon ' \
       'flag-icon-us mr-10"></span>United States</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/5690366"><i class="fa fa-map-marker pr-5 pl-5"></i>Mandan</a> ' \
       '</td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--rainy_river">America/Rainy_River</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--rankin_inlet">America/Rankin_Inlet</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--regina">America/Regina</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6141256"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saskatoon</a>, <a href="https://www.zeitverschiebung.net/cn/city/6119109"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Regina</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6113335"><i class="fa fa-map-marker pr-5 pl-5"></i>Prince ' \
       'Albert</a>, <a href="https://www.zeitverschiebung.net/cn/city/6078112"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Moose Jaw</a>, <a href="https://www.zeitverschiebung.net/cn/city/6089404"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>North Battleford</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--resolute">America/Resolute</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--swift_current">America/Swift_Current</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6160603"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Swift Current</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--tegucigalpa">America/Tegucigalpa</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/hn"><span class="flag-icon flag-icon-hn ' \
       'mr-10"></span>Honduras</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3600949"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tegucigalpa</a>, <a href="https://www.zeitverschiebung.net/cn/city/3601782"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Pedro Sula</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3613533"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Choloma</a>, <a href="https://www.zeitverschiebung.net/cn/city/3608248"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>La Ceiba</a>, <a href="https://www.zeitverschiebung.net/cn/city/3610613"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>El Progreso</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--winnipeg">America/Winnipeg</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6183235"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Winnipeg</a>, <a href="https://www.zeitverschiebung.net/cn/city/5907896"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Brandon</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6111529"><i class="fa fa-map-marker pr-5 pl-5"></i>Portage ' \
       'la Prairie</a>, <a href="https://www.zeitverschiebung.net/cn/city/6165406"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Thompson</a>, <a href="https://www.zeitverschiebung.net/cn/city/6144054"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Selkirk</a> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--easter">Pacific/Easter</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cl"><span class="flag-icon flag-icon-cl ' \
       'mr-10"></span>Chile</a></td> <td> </td> </tr> <tr> <td><strong>UTC-6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--galapagos">Pacific/Galapagos</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ec"><span class="flag-icon flag-icon-ec ' \
       'mr-10"></span>Ecuador</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3652764"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Puerto Ayora</a>, <a href="https://www.zeitverschiebung.net/cn/city/3652758"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Puerto Baquerizo Moreno</a> </td> </tr> <tr> ' \
       '<td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--atikokan">America/Atikokan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--bogota">America/Bogota</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/co"><span class="flag-icon flag-icon-co ' \
       'mr-10"></span>Colombia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3688689"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bogotá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3687925"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cali</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3674962"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Medellín</a>, <a href="https://www.zeitverschiebung.net/cn/city/3689147"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Barranquilla</a>, <a href="https://www.zeitverschiebung.net/cn/city/3687238"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cartagena</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--cancun">America/Cancun</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mx"><span class="flag-icon flag-icon-mx ' \
       'mr-10"></span>Mexico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3531673"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cancún</a>, <a href="https://www.zeitverschiebung.net/cn/city/3531023"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chetumal</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3521342"><i class="fa fa-map-marker pr-5 pl-5"></i>Playa ' \
       'del Carmen</a>, <a href="https://www.zeitverschiebung.net/cn/city/3530103"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>San Miguel de Cozumel</a>, <a href="https://www.zeitverschiebung.net/cn/city/3527639"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Felipe Carrillo Puerto</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--cayman">America/Cayman</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ky"><span class="flag-icon flag-icon-ky ' \
       'mr-10"></span>Cayman Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3580661"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>George Town</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3580477"><i class="fa fa-map-marker pr-5 pl-5"></i>West ' \
       'Bay</a>, <a href="https://www.zeitverschiebung.net/cn/city/3580733"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bodden Town</a>, <a href="https://www.zeitverschiebung.net/cn/city/3580678"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>East End</a>, <a href="https://www.zeitverschiebung.net/cn/city/3580575"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>North Side</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--detroit">America/Detroit</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4990729"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Detroit</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4994358"><i class="fa fa-map-marker pr-5 pl-5"></i>Grand ' \
       'Rapids</a>, <a href="https://www.zeitverschiebung.net/cn/city/5014051"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Warren</a>, <a href="https://www.zeitverschiebung.net/cn/city/5011148"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sterling Heights</a>, <a href="https://www.zeitverschiebung.net/cn/city/4998830"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lansing</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--eirunepe">America/Eirunepe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3664321"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Eirunepé</a>, <a href="https://www.zeitverschiebung.net/cn/city/3665016"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Benjamin Constant</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3664301"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Envira</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--grand_turk">America/Grand_Turk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tc"><span class="flag-icon flag-icon-tc mr-10"></span>Turks ' \
       'and Caicos Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3576994"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cockburn Town</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--guayaquil">America/Guayaquil</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ec"><span class="flag-icon flag-icon-ec ' \
       'mr-10"></span>Ecuador</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3657509"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Guayaquil</a>, <a href="https://www.zeitverschiebung.net/cn/city/3652462"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Quito</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3658666"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Cuenca</a>, <a href="https://www.zeitverschiebung.net/cn/city/3651297"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Santo Domingo de los Colorados</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3654533"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Machala</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--havana">America/Havana</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cu"><span class="flag-icon flag-icon-cu ' \
       'mr-10"></span>Cuba</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3553478"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Havana</a>, <a href="https://www.zeitverschiebung.net/cn/city/3536729"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Santiago de Cuba</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3566067"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Camagüey</a>, <a href="https://www.zeitverschiebung.net/cn/city/3556969"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Holguín</a>, <a href="https://www.zeitverschiebung.net/cn/city/3557689"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Guantánamo</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--indianapolis">America/Indiana' \
       '/Indianapolis</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon ' \
       'flag-icon-us mr-10"></span>United States</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/4259418"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Indianapolis</a>, <a href="https://www.zeitverschiebung.net/cn/city/4920423"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Fort Wayne</a>, <a href="https://www.zeitverschiebung.net/cn/city/4926563"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>South Bend</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4254679"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bloomington</a>, <a href="https://www.zeitverschiebung.net/cn/city/4255466"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Carmel</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--marengo">America/Indiana/Marengo</a></td' \
       '> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--petersburg">America/Indiana/Petersburg' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--vevay">America/Indiana/Vevay</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--vincennes">America/Indiana/Vincennes</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4266307"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Vincennes</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4259640"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Jasper</a>, <a href="https://www.zeitverschiebung.net/cn/city/4266586"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Washington</a>, <a href="https://www.zeitverschiebung.net/cn/city/4259271"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Huntingburg</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--indiana--winamac">America/Indiana/Winamac</a></td' \
       '> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--iqaluit">America/Iqaluit</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5983720"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Iqaluit</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--jamaica">America/Jamaica</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/jm"><span class="flag-icon flag-icon-jm ' \
       'mr-10"></span>Jamaica</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3489854"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kingston</a>, <a href="https://www.zeitverschiebung.net/cn/city/3489297"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>New Kingston</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3488465"><i class="fa fa-map-marker pr-5 pl-5"></i>Spanish ' \
       'Town</a>, <a href="https://www.zeitverschiebung.net/cn/city/3488981"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Portmore</a>, <a href="https://www.zeitverschiebung.net/cn/city/3489460"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Montego Bay</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--kentucky--louisville">America/Kentucky/Louisville' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4299276"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Louisville</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4259671"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Jeffersonville</a>, <a href="https://www.zeitverschiebung.net/cn/city/4262045"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>New Albany</a>, <a href="https://www.zeitverschiebung.net/cn/city/4296218"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Jeffersontown</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4304713"><i class="fa fa-map-marker pr-5 pl-5"></i>Pleasure ' \
       'Ridge Park</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--kentucky--monticello">America/Kentucky/Monticello' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4301224"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Monticello</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--lima">America/Lima</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pe"><span class="flag-icon flag-icon-pe ' \
       'mr-10"></span>Peru</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3936456"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lima</a>, <a href="https://www.zeitverschiebung.net/cn/city/3947322"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Arequipa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3946083"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Callao</a>, <a href="https://www.zeitverschiebung.net/cn/city/3691175"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Trujillo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3698350"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chiclayo</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--nassau">America/Nassau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bs"><span class="flag-icon flag-icon-bs ' \
       'mr-10"></span>Bahamas</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3571824"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nassau</a>, <a href="https://www.zeitverschiebung.net/cn/city/3571971"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lucaya</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3572375"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Freeport</a>, <a href="https://www.zeitverschiebung.net/cn/city/3571224"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>West End</a>, <a href="https://www.zeitverschiebung.net/cn/city/3572601"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cooper’s Town</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--new_york">America/New_York</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/us"><span class="flag-icon flag-icon-us ' \
       'mr-10"></span>United States</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5128581"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>New York City</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5110302"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Brooklyn</a>, <a href="https://www.zeitverschiebung.net/cn/city/5133273"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Borough of Queens</a>, <a href="https://www.zeitverschiebung.net/cn/city/4560349"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Philadelphia</a>, <a href="https://www.zeitverschiebung.net/cn/city/5125771"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Manhattan</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--nipigon">America/Nipigon</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--panama">America/Panama</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pa"><span class="flag-icon flag-icon-pa ' \
       'mr-10"></span>Panama</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3703443"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Panamá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3701329"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Miguelito</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3700563"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tocumen</a>, <a href="https://www.zeitverschiebung.net/cn/city/3711668"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>David</a>, <a href="https://www.zeitverschiebung.net/cn/city/3714637"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Arraiján</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--pangnirtung">America/Pangnirtung</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--port-au-prince">America/Port-au-Prince</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ht"><span class="flag-icon flag-icon-ht ' \
       'mr-10"></span>Haiti</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3718426"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Port-au-Prince</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3728338"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Carrefour</a>, <a href="https://www.zeitverschiebung.net/cn/city/3726786"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Delmas 73</a>, <a href="https://www.zeitverschiebung.net/cn/city/3719028"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pétionville</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3718420"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Port-de-Paix</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--rio_branco">America/Rio_Branco</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3662574"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rio Branco</a>, <a href="https://www.zeitverschiebung.net/cn/city/3664464"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cruzeiro do Sul</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3662155"><i class="fa fa-map-marker pr-5 pl-5"></i>Sena ' \
       'Madureira</a>, <a href="https://www.zeitverschiebung.net/cn/city/3661980"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tarauacá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3664243"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Feijó</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--thunder_bay">America/Thunder_Bay</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6166142"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Thunder Bay</a> </td> </tr> <tr> <td><strong>UTC-5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--toronto">America/Toronto</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6167865"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Toronto</a>, <a href="https://www.zeitverschiebung.net/cn/city/6077243"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Montréal</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6094817"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ottawa</a>, <a href="https://www.zeitverschiebung.net/cn/city/6075357"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mississauga</a>, <a href="https://www.zeitverschiebung.net/cn/city/6091104"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>North York</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--anguilla">America/Anguilla</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ai"><span class="flag-icon flag-icon-ai ' \
       'mr-10"></span>Anguilla</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3573374"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>The Valley</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--antigua">America/Antigua</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ag"><span class="flag-icon flag-icon-ag ' \
       'mr-10"></span>Antigua and Barbuda</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3576022"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saint John’s</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3576057"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Piggotts</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576361"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bolands</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576311"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Codrington</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576074"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Parham</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--aruba">America/Aruba</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aw"><span class="flag-icon flag-icon-aw ' \
       'mr-10"></span>Aruba</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3577277"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Babijn</a>, <a href="https://www.zeitverschiebung.net/cn/city/3577154"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Oranjestad</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3577284"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Angochi</a>, <a href="https://www.zeitverschiebung.net/cn/city/3577282"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Arasji</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--asuncion">America/Asuncion</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/py"><span class="flag-icon flag-icon-py ' \
       'mr-10"></span>Paraguay</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3439389"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Asunción</a>, <a href="https://www.zeitverschiebung.net/cn/city/3439101"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ciudad del Este</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3437056"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Lorenzo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3439214"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Capiatá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3437863"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Lambaré</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--barbados">America/Barbados</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bb"><span class="flag-icon flag-icon-bb ' \
       'mr-10"></span>Barbados</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3374036"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bridgetown</a>, <a href="https://www.zeitverschiebung.net/cn/city/3373505"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Speightstown</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3373652"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Oistins</a>, <a href="https://www.zeitverschiebung.net/cn/city/3374083"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bathsheba</a>, <a href="https://www.zeitverschiebung.net/cn/city/3373790"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Holetown</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--blanc-sablon">America/Blanc-Sablon</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6325521"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lévis</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--boa_vista">America/Boa_Vista</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3664980"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Boa Vista</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--campo_grande">America/Campo_Grande</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3467747"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Campo Grande</a>, <a href="https://www.zeitverschiebung.net/cn/city/3464460"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dourados</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3465342"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Corumbá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3446098"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Três Lagoas</a>, <a href="https://www.zeitverschiebung.net/cn/city/3453150"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ponta Porã</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--caracas">America/Caracas</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ve"><span class="flag-icon flag-icon-ve ' \
       'mr-10"></span>Venezuela</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3646738"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Caracas</a>, <a href="https://www.zeitverschiebung.net/cn/city/3633009"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maracaibo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3632998"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Maracay</a>, <a href="https://www.zeitverschiebung.net/cn/city/3625549"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Valencia</a>, <a href="https://www.zeitverschiebung.net/cn/city/3648522"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Barquisimeto</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--cuiaba">America/Cuiaba</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3465038"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cuiabá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3445451"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Várzea Grande</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3450909"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Rondonópolis</a>, <a href="https://www.zeitverschiebung.net/cn/city/6318696"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sinop</a>, <a href="https://www.zeitverschiebung.net/cn/city/3470709"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Barra do Garças</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--curacao">America/Curacao</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cw"><span class="flag-icon flag-icon-cw ' \
       'mr-10"></span>Curacao</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3513090"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Willemstad</a>, <a href="https://www.zeitverschiebung.net/cn/city/3513221"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sint Michiel Liber</a> </td> </tr> <tr> ' \
       '<td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--dominica">America/Dominica</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/dm"><span class="flag-icon flag-icon-dm ' \
       'mr-10"></span>Dominica</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3575635"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Roseau</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575654"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Portsmouth</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3575899"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Berekua</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575624"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Saint Joseph</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575568"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Wesley</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--glace_bay">America/Glace_Bay</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6354908"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sydney</a>, <a href="https://www.zeitverschiebung.net/cn/city/5961564"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Glace Bay</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7303783"><i class="fa fa-map-marker pr-5 pl-5"></i>Sydney ' \
       'Mines</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--goose_bay">America/Goose_Bay</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/5994839"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Labrador City</a>, <a href="https://www.zeitverschiebung.net/cn/city/5970458"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Happy Valley-Goose Bay</a> </td> </tr> <tr> ' \
       '<td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--grenada">America/Grenada</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gd"><span class="flag-icon flag-icon-gd ' \
       'mr-10"></span>Grenada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3579925"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint George"s</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3580279"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Gouyave</a>, <a href="https://www.zeitverschiebung.net/cn/city/3580236"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Grenville</a>, <a href="https://www.zeitverschiebung.net/cn/city/3579833"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Victoria</a>, <a href="https://www.zeitverschiebung.net/cn/city/3579931"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saint David’s</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--guadeloupe">America/Guadeloupe</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/gp"><span class="flag-icon flag-icon-gp ' \
       'mr-10"></span>Guadeloupe</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3578959"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Les Abymes</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3579767"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Baie-Mahault</a>, <a href="https://www.zeitverschiebung.net/cn/city/3578978"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Le Gosier</a>, <a href="https://www.zeitverschiebung.net/cn/city/3578682"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Petit-Bourg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3578466"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sainte-Anne</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--guyana">America/Guyana</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gy"><span class="flag-icon flag-icon-gy ' \
       'mr-10"></span>Guyana</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3378644"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Georgetown</a>, <a href="https://www.zeitverschiebung.net/cn/city/3377408"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Linden</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3376762"><i class="fa fa-map-marker pr-5 pl-5"></i>New ' \
       'Amsterdam</a>, <a href="https://www.zeitverschiebung.net/cn/city/7303406"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Anna Regina</a>, <a href="https://www.zeitverschiebung.net/cn/city/3379507"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bartica</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--halifax">America/Halifax</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6324729"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Halifax</a>, <a href="https://www.zeitverschiebung.net/cn/city/5935277"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dartmouth</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5920288"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Charlottetown</a>, <a href="https://www.zeitverschiebung.net/cn/city/10287505"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lower Sacvkille</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6169587"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Truro</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--kralendijk">America/Kralendijk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bq"><span class="flag-icon flag-icon-bq ' \
       'mr-10"></span>Bonaire, Saint Eustatius and Saba </a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/3513563"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kralendijk</a>, <a href="https://www.zeitverschiebung.net/cn/city/3513426"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Oranjestad</a>, <a href="https://www.zeitverschiebung.net/cn/city/3513173"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>The Bottom</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--la_paz">America/La_Paz</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bo"><span class="flag-icon flag-icon-bo ' \
       'mr-10"></span>Bolivia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3904906"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Santa Cruz de la Sierra</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3919968"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Cochabamba</a>, <a href="https://www.zeitverschiebung.net/cn/city/3911925"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>La Paz</a>, <a href="https://www.zeitverschiebung.net/cn/city/3903987"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sucre</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3909234"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Oruro</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--lower_princes">America/Lower_Princes</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/sx"><span class="flag-icon flag-icon-sx ' \
       'mr-10"></span>Sint Maarten</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3513794"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cul de Sac</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3513392"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Philipsburg</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--manaus">America/Manaus</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3663517"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Manaus</a>, <a href="https://www.zeitverschiebung.net/cn/city/3397893"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Itacoatiara</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3393008"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Parintins</a>, <a href="https://www.zeitverschiebung.net/cn/city/3663529"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Manacapuru</a>, <a href="https://www.zeitverschiebung.net/cn/city/3664539"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Coari</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--marigot">America/Marigot</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mf"><span class="flag-icon flag-icon-mf mr-10"></span>Saint ' \
       'Martin</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3578851"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Marigot</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--martinique">America/Martinique</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mq"><span class="flag-icon flag-icon-mq ' \
       'mr-10"></span>Martinique</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3570675"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Fort-de-France</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3570428"><i class="fa fa-map-marker pr-5 pl-5"></i>Le ' \
       'Lamentin</a>, <a href="https://www.zeitverschiebung.net/cn/city/3570412"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Le Robert</a>, <a href="https://www.zeitverschiebung.net/cn/city/3569926"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sainte-Marie</a>, <a href="https://www.zeitverschiebung.net/cn/city/3570429"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Le François</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--moncton">America/Moncton</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6138517"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint John</a>, <a href="https://www.zeitverschiebung.net/cn/city/6076211"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Moncton</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5957776"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Fredericton</a>, <a href="https://www.zeitverschiebung.net/cn/city/5939219"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dieppe</a>, <a href="https://www.zeitverschiebung.net/cn/city/6075081"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Miramichi</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--montserrat">America/Montserrat</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ms"><span class="flag-icon flag-icon-ms ' \
       'mr-10"></span>Montserrat</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/7266440"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Brades</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3578038"><i class="fa fa-map-marker pr-5 pl-5"></i>Saint ' \
       'Peters</a>, <a href="https://www.zeitverschiebung.net/cn/city/3578069"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Plymouth</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--porto_velho">America/Porto_Velho</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3662762"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Porto Velho</a>, <a href="https://www.zeitverschiebung.net/cn/city/3925033"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ji Paraná</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3924679"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Vilhena</a>, <a href="https://www.zeitverschiebung.net/cn/city/3665199"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ariquemes</a>, <a href="https://www.zeitverschiebung.net/cn/city/3925212"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cacoal</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--port_of_spain">America/Port_of_Spain</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/tt"><span class="flag-icon flag-icon-tt ' \
       'mr-10"></span>Trinidad and Tobago</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3574309"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Laventille</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3574810"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Chaguanas</a>, <a href="https://www.zeitverschiebung.net/cn/city/3574116"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mon Repos</a>, <a href="https://www.zeitverschiebung.net/cn/city/3573738"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Fernando</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3573890"><i class="fa fa-map-marker pr-5 pl-5"></i>Port of ' \
       'Spain</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--puerto_rico">America/Puerto_Rico</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pr"><span class="flag-icon flag-icon-pr ' \
       'mr-10"></span>Puerto Rico</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4568127"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Juan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4562831"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bayamón</a>, <a href="https://www.zeitverschiebung.net/cn/city/4563243"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Carolina</a>, <a href="https://www.zeitverschiebung.net/cn/city/4566880"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ponce</a>, <a href="https://www.zeitverschiebung.net/cn/city/4563008"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Caguas</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--santiago">America/Santiago</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cl"><span class="flag-icon flag-icon-cl ' \
       'mr-10"></span>Chile</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3871336"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Santiago</a>, <a href="https://www.zeitverschiebung.net/cn/city/3875024"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Puente Alto</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3899539"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Antofagasta</a>, <a href="https://www.zeitverschiebung.net/cn/city/3868121"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Viña del Mar</a>, <a href="https://www.zeitverschiebung.net/cn/city/3868626"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Valparaíso</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--santo_domingo">America/Santo_Domingo</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/do"><span class="flag-icon flag-icon-do ' \
       'mr-10"></span>Dominican Republic</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3492908"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Santo Domingo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3492914"><i class="fa fa-map-marker pr-5 pl-5"></i>Santiago ' \
       'de los Caballeros</a>, <a href="https://www.zeitverschiebung.net/cn/city/7874116"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Santo Domingo Oeste</a>, <a href="https://www.zeitverschiebung.net/cn/city/3493032"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Pedro de Macorís</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3500957"><i class="fa fa-map-marker pr-5 pl-5"></i>La ' \
       'Romana</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_barthelemy">America/St_Barthelemy</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/bl"><span class="flag-icon flag-icon-bl ' \
       'mr-10"></span>Saint Barthelemy</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3579132"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gustavia</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_kitts">America/St_Kitts</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kn"><span class="flag-icon flag-icon-kn mr-10"></span>Saint ' \
       'Kitts and Nevis</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3575551"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Basseterre</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575423"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Fig Tree</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3575296"><i class="fa fa-map-marker pr-5 pl-5"></i>Market ' \
       'Shop</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575170"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Saint Paul’s</a>, <a href="https://www.zeitverschiebung.net/cn/city/3575292"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Middle Island</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_lucia">America/St_Lucia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lc"><span class="flag-icon flag-icon-lc mr-10"></span>Saint ' \
       'Lucia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3576812"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Castries</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576854"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bisée</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576414"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Vieux Fort</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3576569"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Micoud</a>, <a href="https://www.zeitverschiebung.net/cn/city/3576442"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Soufrière</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_thomas">America/St_Thomas</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/vi"><span class="flag-icon flag-icon-vi mr-10"></span>U.S. ' \
       'Virgin Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4796512"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint Croix</a>, <a href="https://www.zeitverschiebung.net/cn/city/4795467"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Charlotte Amalie</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4795577"><i class="fa fa-map-marker pr-5 pl-5"></i>Cruz ' \
       'Bay</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_vincent">America/St_Vincent</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/vc"><span class="flag-icon flag-icon-vc mr-10"></span>Saint ' \
       'Vincent and the Grenadines</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3577887"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kingstown</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3748726"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kingstown Park</a>, <a href="https://www.zeitverschiebung.net/cn/city/3577900"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Georgetown</a>, <a href="https://www.zeitverschiebung.net/cn/city/3577962"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Barrouallie</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3577844"><i class="fa fa-map-marker pr-5 pl-5"></i>Port ' \
       'Elizabeth</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--thule">America/Thule</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gl"><span class="flag-icon flag-icon-gl ' \
       'mr-10"></span>Greenland</a></td> <td> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--tortola">America/Tortola</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/vg"><span class="flag-icon flag-icon-vg ' \
       'mr-10"></span>British Virgin Islands</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/8533874"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tortola</a>, <a href="https://www.zeitverschiebung.net/cn/city/3577430"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Road Town</a> </td> </tr> <tr> <td><strong>UTC-4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--bermuda">Atlantic/Bermuda</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bm"><span class="flag-icon flag-icon-bm ' \
       'mr-10"></span>Bermuda</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3573197"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hamilton</a> </td> </tr> <tr> <td><strong>UTC-3:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--st_johns">America/St_Johns</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ca"><span class="flag-icon flag-icon-ca ' \
       'mr-10"></span>Canada</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6324733"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>St. John"s</a>, <a href="https://www.zeitverschiebung.net/cn/city/6082231"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mount Pearl</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/5927969"><i class="fa fa-map-marker pr-5 pl-5"></i>Corner ' \
       'Brook</a>, <a href="https://www.zeitverschiebung.net/cn/city/5926511"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Conception Bay South</a>, <a href="https://www.zeitverschiebung.net/cn/city/5895424"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bay Roberts</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--araguaina">America/Araguaina</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3474574"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Palmas</a>, <a href="https://www.zeitverschiebung.net/cn/city/3407357"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Araguaína</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3461724"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Gurupi</a>, <a href="https://www.zeitverschiebung.net/cn/city/3391371"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Porto Franco</a>, <a href="https://www.zeitverschiebung.net/cn/city/3447075"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Taguatinga</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--buenos_aires">America/Argentina' \
       '/Buenos_Aires</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon ' \
       'flag-icon-ar mr-10"></span>Argentina</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/3435910"><i class="fa fa-map-marker pr-5 pl-5"></i>Buenos ' \
       'Aires</a>, <a href="https://www.zeitverschiebung.net/cn/city/3432043"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>La Plata</a>, <a href="https://www.zeitverschiebung.net/cn/city/3430863"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mar del Plata</a>, <a href="https://www.zeitverschiebung.net/cn/city/3429652"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Quilmes</a>, <a href="https://www.zeitverschiebung.net/cn/city/3430545"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Morón</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--catamarca">America/Argentina/Catamarca' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3837702"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Fernando del Valle de Catamarca</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3860443"><i class="fa fa-map-marker pr-5 pl-5"></i>Comodoro ' \
       'Rivadavia</a>, <a href="https://www.zeitverschiebung.net/cn/city/3833883"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Trelew</a>, <a href="https://www.zeitverschiebung.net/cn/city/3840092"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Puerto Madryn</a>, <a href="https://www.zeitverschiebung.net/cn/city/3855974"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Esquel</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--cordoba">America/Argentina/Cordoba</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3860259"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Córdoba</a>, <a href="https://www.zeitverschiebung.net/cn/city/3838583"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rosario</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3836277"><i class="fa fa-map-marker pr-5 pl-5"></i>Santa Fe ' \
       'de la Vera Cruz</a>, <a href="https://www.zeitverschiebung.net/cn/city/3429577"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Resistencia</a>, <a href="https://www.zeitverschiebung.net/cn/city/3835869"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Santiago del Estero</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--jujuy">America/Argentina/Jujuy</a></td' \
       '> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3836564"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Salvador de Jujuy</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3836772"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Pedro</a>, <a href="https://www.zeitverschiebung.net/cn/city/3846915"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Libertador General San Martín</a>, <a href="https://www.zeitverschiebung.net/cn/city/3842190"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Palpalá</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3849140"><i class="fa fa-map-marker pr-5 pl-5"></i>La ' \
       'Quiaca</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--la_rioja">America/Argentina/La_Rioja' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3848950"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>La Rioja</a>, <a href="https://www.zeitverschiebung.net/cn/city/3861445"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chilecito</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3865579"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Arauco</a>, <a href="https://www.zeitverschiebung.net/cn/city/3861824"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Chamical</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--mendoza">America/Argentina/Mendoza</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3844421"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mendoza</a>, <a href="https://www.zeitverschiebung.net/cn/city/3836669"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>San Rafael</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3836992"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Martín</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--rio_gallegos">America/Argentina' \
       '/Rio_Gallegos</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon ' \
       'flag-icon-ar mr-10"></span>Argentina</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/3838859"><i class="fa fa-map-marker pr-5 pl-5"></i>Río ' \
       'Gallegos</a>, <a href="https://www.zeitverschiebung.net/cn/city/3863379"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Caleta Olivia</a>, <a href="https://www.zeitverschiebung.net/cn/city/3841309"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pico Truncado</a>, <a href="https://www.zeitverschiebung.net/cn/city/3840104"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Puerto Deseado</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3848353"><i class="fa fa-map-marker pr-5 pl-5"></i>Las ' \
       'Heras</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--salta">America/Argentina/Salta</a></td' \
       '> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3838233"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Salta</a>, <a href="https://www.zeitverschiebung.net/cn/city/3843123"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Neuquén</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3835994"><i class="fa fa-map-marker pr-5 pl-5"></i>Santa ' \
       'Rosa</a>, <a href="https://www.zeitverschiebung.net/cn/city/7647007"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>San Carlos de Bariloche</a>, <a href="https://www.zeitverschiebung.net/cn/city/3861056"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cipolletti</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--san_juan">America/Argentina/San_Juan' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3837213"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Juan</a>, <a href="https://www.zeitverschiebung.net/cn/city/3861416"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chimbas</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3836194"><i class="fa fa-map-marker pr-5 pl-5"></i>Santa ' \
       'Lucía</a>, <a href="https://www.zeitverschiebung.net/cn/city/3840860"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Pocito</a>, <a href="https://www.zeitverschiebung.net/cn/city/3862240"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Caucete</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--san_luis">America/Argentina/San_Luis' \
       '</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3837056"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Luis</a>, <a href="https://www.zeitverschiebung.net/cn/city/7116866"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Villa Mercedes</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7284819"><i class="fa fa-map-marker pr-5 pl-5"></i>La ' \
       'Punta</a>, <a href="https://www.zeitverschiebung.net/cn/city/3844377"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Merlo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3853330"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Justo Daract</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--tucuman">America/Argentina/Tucuman</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3836873"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Miguel de Tucumán</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3832260"><i class="fa fa-map-marker pr-5 pl-5"></i>Yerba ' \
       'Buena</a>, <a href="https://www.zeitverschiebung.net/cn/city/3834813"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tafí Viejo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3866367"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Alderetes</a>, <a href="https://www.zeitverschiebung.net/cn/city/3866496"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Aguilares</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--argentina--ushuaia">America/Argentina/Ushuaia</a' \
       '></td> <td><a href="https://www.zeitverschiebung.net/cn/country/ar"><span class="flag-icon flag-icon-ar ' \
       'mr-10"></span>Argentina</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3833367"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ushuaia</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--bahia">America/Bahia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3450554"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Salvador</a>, <a href="https://www.zeitverschiebung.net/cn/city/3463478"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Feira de Santana</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3444914"><i class="fa fa-map-marker pr-5 pl-5"></i>Vitória ' \
       'da Conquista</a>, <a href="https://www.zeitverschiebung.net/cn/city/3460949"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Itabuna</a>, <a href="https://www.zeitverschiebung.net/cn/city/3468031"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Camaçari</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--belem">America/Belem</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3405870"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Belém</a>, <a href="https://www.zeitverschiebung.net/cn/city/3407669"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ananindeua</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3396016"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Macapá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3395503"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Marabá</a>, <a href="https://www.zeitverschiebung.net/cn/city/3402591"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Castanhal</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--cayenne">America/Cayenne</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gf"><span class="flag-icon flag-icon-gf ' \
       'mr-10"></span>French Guiana</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3382160"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cayenne</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3380965"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Matoury</a>, <a href="https://www.zeitverschiebung.net/cn/city/3380387"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Saint-Laurent-du-Maroni</a>, <a href="https://www.zeitverschiebung.net/cn/city/3381303"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kourou</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3380892"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Rémire-Montjoly</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--fortaleza">America/Fortaleza</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3399415"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Fortaleza</a>, <a href="https://www.zeitverschiebung.net/cn/city/3388368"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>São Luís</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3394023"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Natal</a>, <a href="https://www.zeitverschiebung.net/cn/city/3386496"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Teresina</a>, <a href="https://www.zeitverschiebung.net/cn/city/3397277"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>João Pessoa</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--godthab">America/Godthab</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gl"><span class="flag-icon flag-icon-gl ' \
       'mr-10"></span>Greenland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3421319"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nuuk</a>, <a href="https://www.zeitverschiebung.net/cn/city/3419842"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sisimiut</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3423146"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ilulissat</a>, <a href="https://www.zeitverschiebung.net/cn/city/3420846"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Qaqortoq</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--maceio">America/Maceio</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3395981"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Maceió</a>, <a href="https://www.zeitverschiebung.net/cn/city/3471872"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Aracaju</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3407327"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Arapiraca</a>, <a href="https://www.zeitverschiebung.net/cn/city/3456223"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nossa Senhora do Socorro</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3449310"><i class="fa fa-map-marker pr-5 pl-5"></i>São ' \
       'Cristóvão</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--miquelon">America/Miquelon</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pm"><span class="flag-icon flag-icon-pm mr-10"></span>Saint ' \
       'Pierre and Miquelon</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3424934"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint-Pierre</a>, <a href="https://www.zeitverschiebung.net/cn/city/3424941"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Miquelon</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--montevideo">America/Montevideo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/uy"><span class="flag-icon flag-icon-uy ' \
       'mr-10"></span>Uruguay</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3441575"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Montevideo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3440714"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Salto</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3441243"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Paysandú</a>, <a href="https://www.zeitverschiebung.net/cn/city/3442057"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Las Piedras</a>, <a href="https://www.zeitverschiebung.net/cn/city/3440781"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rivera</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--paramaribo">America/Paramaribo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sr"><span class="flag-icon flag-icon-sr ' \
       'mr-10"></span>Suriname</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3383330"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Paramaribo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3383714"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lelydorp</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3384482"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Brokopondo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3383427"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nieuw Nickerie</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3383494"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Moengo</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--punta_arenas">America/Punta_Arenas</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/cl"><span class="flag-icon flag-icon-cl ' \
       'mr-10"></span>Chile</a></td> <td> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--recife">America/Recife</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3390760"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Recife</a>, <a href="https://www.zeitverschiebung.net/cn/city/3397838"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Jaboatão</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6317344"><i class="fa fa-map-marker pr-5 pl-5"></i>Jaboatão ' \
       'dos Guararapes</a>, <a href="https://www.zeitverschiebung.net/cn/city/3393536"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Olinda</a>, <a href="https://www.zeitverschiebung.net/cn/city/3392740"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Paulista</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--santarem">America/Santarem</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3389353"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Santarém</a>, <a href="https://www.zeitverschiebung.net/cn/city/3407882"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Altamira</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3397967"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Itaituba</a>, <a href="https://www.zeitverschiebung.net/cn/city/3393471"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Oriximiná</a>, <a href="https://www.zeitverschiebung.net/cn/city/3407980"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Alenquer</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--sao_paulo">America/Sao_Paulo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3448439"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>São Paulo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3451190"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rio de Janeiro</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3470127"><i class="fa fa-map-marker pr-5 pl-5"></i>Belo ' \
       'Horizonte</a>, <a href="https://www.zeitverschiebung.net/cn/city/3469058"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Brasília</a>, <a href="https://www.zeitverschiebung.net/cn/city/3464975"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Curitiba</a> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--palmer">Antarctica/Palmer</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--rothera">Antarctica/Rothera</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC-3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--stanley">Atlantic/Stanley</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fk"><span class="flag-icon flag-icon-fk ' \
       'mr-10"></span>Falkland Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3426691"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Stanley</a> </td> </tr> <tr> <td><strong>UTC-2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--noronha">America/Noronha</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/br"><span class="flag-icon flag-icon-br ' \
       'mr-10"></span>Brazil</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3397963"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Itamaracá</a> </td> </tr> <tr> <td><strong>UTC-2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--south_georgia">Atlantic/South_Georgia</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/gs"><span class="flag-icon flag-icon-gs ' \
       'mr-10"></span>South Georgia and the South Sandwich Islands</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/3426466"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Grytviken</a> </td> </tr> <tr> <td><strong>UTC-1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/america--scoresbysund">America/Scoresbysund</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/gl"><span class="flag-icon flag-icon-gl ' \
       'mr-10"></span>Greenland</a></td> <td> </td> </tr> <tr> <td><strong>UTC-1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--azores">Atlantic/Azores</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pt"><span class="flag-icon flag-icon-pt ' \
       'mr-10"></span>Portugal</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3372783"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ponta Delgada</a>, <a href="https://www.zeitverschiebung.net/cn/city/3373348"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Angra do Heroísmo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3372964"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Lagoa</a>, <a href="https://www.zeitverschiebung.net/cn/city/3372677"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Rosto de Cão</a>, <a href="https://www.zeitverschiebung.net/cn/city/3372745"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rabo de Peixe</a> </td> </tr> <tr> <td><strong>UTC-1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--cape_verde">Atlantic/Cape_Verde</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cv"><span class="flag-icon flag-icon-cv mr-10"></span>Cape ' \
       'Verde</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3374333"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Praia</a>, <a href="https://www.zeitverschiebung.net/cn/city/3374462"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mindelo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3374218"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Santa Maria</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3374707"><i class="fa fa-map-marker pr-5 pl-5"></i>Cova ' \
       'Figueira</a>, <a href="https://www.zeitverschiebung.net/cn/city/3374221"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Santa Cruz</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--abidjan">Africa/Abidjan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ci"><span class="flag-icon flag-icon-ci mr-10"></span>Ivory ' \
       'Coast</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2293538"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Abidjan</a>, <a href="https://www.zeitverschiebung.net/cn/city/2293521"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Abobo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2290956"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bouaké</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2290486"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Daloa</a>, <a href="https://www.zeitverschiebung.net/cn/city/2282006"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>San-Pédro</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--accra">Africa/Accra</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gh"><span class="flag-icon flag-icon-gh ' \
       'mr-10"></span>Ghana</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2306104"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Accra</a>, <a href="https://www.zeitverschiebung.net/cn/city/2298890"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kumasi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2294877"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tamale</a>, <a href="https://www.zeitverschiebung.net/cn/city/2294915"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Takoradi</a>, <a href="https://www.zeitverschiebung.net/cn/city/2306079"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Achiaman</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--bamako">Africa/Bamako</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ml"><span class="flag-icon flag-icon-ml ' \
       'mr-10"></span>Mali</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2460596"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bamako</a>, <a href="https://www.zeitverschiebung.net/cn/city/2451185"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sikasso</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2453348"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mopti</a>, <a href="https://www.zeitverschiebung.net/cn/city/2454268"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Koutiala</a>, <a href="https://www.zeitverschiebung.net/cn/city/2451478"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ségou</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--banjul">Africa/Banjul</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gm"><span class="flag-icon flag-icon-gm ' \
       'mr-10"></span>Gambia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2413753"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Brikama</a>, <a href="https://www.zeitverschiebung.net/cn/city/2413920"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bakau</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2413876"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Banjul</a>, <a href="https://www.zeitverschiebung.net/cn/city/2413515"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Farafenni</a>, <a href="https://www.zeitverschiebung.net/cn/city/2412749"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lamin</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--bissau">Africa/Bissau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gw"><span class="flag-icon flag-icon-gw ' \
       'mr-10"></span>Guinea-Bissau</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2374775"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bissau</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2375254"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bafatá</a>, <a href="https://www.zeitverschiebung.net/cn/city/2372532"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Gabú</a>, <a href="https://www.zeitverschiebung.net/cn/city/2374759"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bissorã</a>, <a href="https://www.zeitverschiebung.net/cn/city/2374688"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bolama</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--conakry">Africa/Conakry</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gn"><span class="flag-icon flag-icon-gn ' \
       'mr-10"></span>Guinea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2422488"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Camayenne</a>, <a href="https://www.zeitverschiebung.net/cn/city/2422465"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Conakry</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2416969"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nzérékoré</a>, <a href="https://www.zeitverschiebung.net/cn/city/2419533"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kindia</a>, <a href="https://www.zeitverschiebung.net/cn/city/2419992"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kankan</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--dakar">Africa/Dakar</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sn"><span class="flag-icon flag-icon-sn ' \
       'mr-10"></span>Senegal</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2253354"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dakar</a>, <a href="https://www.zeitverschiebung.net/cn/city/2246678"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pikine</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2244322"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Touba</a>, <a href="https://www.zeitverschiebung.net/cn/city/2244799"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Thiès Nones</a>, <a href="https://www.zeitverschiebung.net/cn/city/2246452"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint-Louis</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--freetown">Africa/Freetown</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sl"><span class="flag-icon flag-icon-sl ' \
       'mr-10"></span>Sierra Leone</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2409306"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Freetown</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2410048"><i class="fa fa-map-marker pr-5 pl-5"></i>Bo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2407790"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kenema</a>, <a href="https://www.zeitverschiebung.net/cn/city/2407656"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Koidu</a>, <a href="https://www.zeitverschiebung.net/cn/city/2406407"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Makeni</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--lome">Africa/Lome</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tg"><span class="flag-icon flag-icon-tg ' \
       'mr-10"></span>Togo</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2365267"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lomé</a>, <a href="https://www.zeitverschiebung.net/cn/city/2364104"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sokodé</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2366152"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kara</a>, <a href="https://www.zeitverschiebung.net/cn/city/2367886"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Atakpamé</a>, <a href="https://www.zeitverschiebung.net/cn/city/2365560"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kpalimé</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--monrovia">Africa/Monrovia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lr"><span class="flag-icon flag-icon-lr ' \
       'mr-10"></span>Liberia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2274895"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Monrovia</a>, <a href="https://www.zeitverschiebung.net/cn/city/2277060"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gbarnga</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2276086"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kakata</a>, <a href="https://www.zeitverschiebung.net/cn/city/2278682"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bensonville</a>, <a href="https://www.zeitverschiebung.net/cn/city/2276492"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Harper</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--nouakchott">Africa/Nouakchott</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mr"><span class="flag-icon flag-icon-mr ' \
       'mr-10"></span>Mauritania</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2377450"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Nouakchott</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2377457"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nouâdhibou</a>, <a href="https://www.zeitverschiebung.net/cn/city/2377539"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Néma</a>, <a href="https://www.zeitverschiebung.net/cn/city/2378736"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kaédi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2376898"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Rosso</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--ouagadougou">Africa/Ouagadougou</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bf"><span class="flag-icon flag-icon-bf ' \
       'mr-10"></span>Burkina Faso</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2357048"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ouagadougou</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2362344"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bobo-Dioulasso</a>, <a href="https://www.zeitverschiebung.net/cn/city/2358946"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Koudougou</a>, <a href="https://www.zeitverschiebung.net/cn/city/2357043"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ouahigouya</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2362909"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Banfora</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--sao_tome">Africa/Sao_Tome</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/st"><span class="flag-icon flag-icon-st mr-10"></span>Sao ' \
       'Tome and Principe</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2410763"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>São Tomé</a>, <a href="https://www.zeitverschiebung.net/cn/city/2410805"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Santo António</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/america--danmarkshavn">America/Danmarkshavn</a></td' \
       '> <td><a href="https://www.zeitverschiebung.net/cn/country/gl"><span class="flag-icon flag-icon-gl ' \
       'mr-10"></span>Greenland</a></td> <td> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--troll">Antarctica/Troll</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--canary">Atlantic/Canary</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/es"><span class="flag-icon flag-icon-es ' \
       'mr-10"></span>Spain</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2515270"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Las Palmas de Gran Canaria</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2511174"><i class="fa fa-map-marker pr-5 pl-5"></i>Santa ' \
       'Cruz de Tenerife</a>, <a href="https://www.zeitverschiebung.net/cn/city/2511401"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>La Laguna</a>, <a href="https://www.zeitverschiebung.net/cn/city/2510542"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Telde</a>, <a href="https://www.zeitverschiebung.net/cn/city/2521582"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Arona</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--faroe">Atlantic/Faroe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fo"><span class="flag-icon flag-icon-fo mr-10"></span>Faroe ' \
       'Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2611396"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tórshavn</a>, <a href="https://www.zeitverschiebung.net/cn/city/2618795"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Klaksvík</a>, <a href="https://www.zeitverschiebung.net/cn/city/2621808"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Fuglafjørður</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2611060"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tvøroyri</a>, <a href="https://www.zeitverschiebung.net/cn/city/2616914"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Miðvágur</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--madeira">Atlantic/Madeira</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pt"><span class="flag-icon flag-icon-pt ' \
       'mr-10"></span>Portugal</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2267827"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Funchal</a>, <a href="https://www.zeitverschiebung.net/cn/city/2270380"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Câmara de Lobos</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2266895"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Machico</a>, <a href="https://www.zeitverschiebung.net/cn/city/2270258"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Caniço</a>, <a href="https://www.zeitverschiebung.net/cn/city/2263491"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Santana</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--reykjavik">Atlantic/Reykjavik</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/is"><span class="flag-icon flag-icon-is ' \
       'mr-10"></span>Iceland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3413829"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Reykjavík</a>, <a href="https://www.zeitverschiebung.net/cn/city/3415212"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kópavogur</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3416706"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hafnarfjörður</a>, <a href="https://www.zeitverschiebung.net/cn/city/2633274"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Akureyri</a>, <a href="https://www.zeitverschiebung.net/cn/city/3417195"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Garðabær</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/atlantic--st_helena">Atlantic/St_Helena</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sh"><span class="flag-icon flag-icon-sh mr-10"></span>Saint ' \
       'Helena</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3370903"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Jamestown</a>, <a href="https://www.zeitverschiebung.net/cn/city/2411397"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Georgetown</a>, <a href="https://www.zeitverschiebung.net/cn/city/3370726"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Edinburgh of the Seven Seas</a> </td> </tr> <tr> ' \
       '<td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--guernsey">Europe/Guernsey</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gg"><span class="flag-icon flag-icon-gg ' \
       'mr-10"></span>Guernsey</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3042287"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint Peter Port</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--isle_of_man">Europe/Isle_of_Man</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/im"><span class="flag-icon flag-icon-im mr-10"></span>Isle ' \
       'of Man</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3042237"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Douglas</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042192"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ramsey</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042198"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Peel</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3042196"><i class="fa fa-map-marker pr-5 pl-5"></i>Port ' \
       'Erin</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042255"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Castletown</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--jersey">Europe/Jersey</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/je"><span class="flag-icon flag-icon-je ' \
       'mr-10"></span>Jersey</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3042091"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint Helier</a>, <a href="https://www.zeitverschiebung.net/cn/city/10942508"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Le Hocq</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--lisbon">Europe/Lisbon</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pt"><span class="flag-icon flag-icon-pt ' \
       'mr-10"></span>Portugal</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2267057"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lisbon</a>, <a href="https://www.zeitverschiebung.net/cn/city/2735943"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Porto</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2271772"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Amadora</a>, <a href="https://www.zeitverschiebung.net/cn/city/2742032"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Braga</a>, <a href="https://www.zeitverschiebung.net/cn/city/2262963"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Setúbal</a> </td> </tr> <tr> <td><strong>UTC+0</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--london">Europe/London</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gb"><span class="flag-icon flag-icon-gb ' \
       'mr-10"></span>United Kingdom</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2643743"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>London</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2643741"><i class="fa fa-map-marker pr-5 pl-5"></i>City of ' \
       'London</a>, <a href="https://www.zeitverschiebung.net/cn/city/2655603"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Birmingham</a>, <a href="https://www.zeitverschiebung.net/cn/city/2648579"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Glasgow</a>, <a href="https://www.zeitverschiebung.net/cn/city/2644210"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Liverpool</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--algiers">Africa/Algiers</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/dz"><span class="flag-icon flag-icon-dz ' \
       'mr-10"></span>Algeria</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2507480"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Algiers</a>, <a href="https://www.zeitverschiebung.net/cn/city/2474141"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Boumerdas</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2485926"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Oran</a>, <a href="https://www.zeitverschiebung.net/cn/city/2477461"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tébessa</a>, <a href="https://www.zeitverschiebung.net/cn/city/2501152"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Constantine</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--bangui">Africa/Bangui</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cf"><span class="flag-icon flag-icon-cf ' \
       'mr-10"></span>Central African Republic</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/2389853"><i class="fa fa-map-marker pr-5 pl-5"></i>Bangui</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2388873"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bimbo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2384770"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mbaïki</a>, <a href="https://www.zeitverschiebung.net/cn/city/2389086"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Berbérati</a>, <a href="https://www.zeitverschiebung.net/cn/city/2386012"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kaga Bandoro</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/africa--brazzaville">Africa/Brazzaville</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/cg"><span class="flag-icon flag-icon-cg ' \
       'mr-10"></span>Republic of the Congo</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/2260535"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Brazzaville</a>, <a href="https://www.zeitverschiebung.net/cn/city/2255414"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pointe-Noire</a>, <a href="https://www.zeitverschiebung.net/cn/city/2258261"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dolisie</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2259383"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kayes</a>, <a href="https://www.zeitverschiebung.net/cn/city/2255542"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Owando</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--casablanca">Africa/Casablanca</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ma"><span class="flag-icon flag-icon-ma ' \
       'mr-10"></span>Morocco</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2553604"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Casablanca</a>, <a href="https://www.zeitverschiebung.net/cn/city/2538475"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rabat</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2548885"><i class="fa fa-map-marker pr-5 pl-5"></i>Fes</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2537763"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sale</a>, <a href="https://www.zeitverschiebung.net/cn/city/2542997"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Marrakesh</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--ceuta">Africa/Ceuta</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/es"><span class="flag-icon flag-icon-es ' \
       'mr-10"></span>Spain</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6362987"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ceuta</a>, <a href="https://www.zeitverschiebung.net/cn/city/2513947"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Melilla</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--douala">Africa/Douala</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cm"><span class="flag-icon flag-icon-cm ' \
       'mr-10"></span>Cameroon</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2232593"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Douala</a>, <a href="https://www.zeitverschiebung.net/cn/city/2220957"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Yaoundé</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2231320"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Garoua</a>, <a href="https://www.zeitverschiebung.net/cn/city/2229798"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kousséri</a>, <a href="https://www.zeitverschiebung.net/cn/city/2234974"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bamenda</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--el_aaiun">Africa/El_Aaiun</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/eh"><span class="flag-icon flag-icon-eh ' \
       'mr-10"></span>Western Sahara</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2463447"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dakhla</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2461874"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Smara</a>, <a href="https://www.zeitverschiebung.net/cn/city/2461993"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Laayoune Plage</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--kinshasa">Africa/Kinshasa</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cd"><span class="flag-icon flag-icon-cd ' \
       'mr-10"></span>Democratic Republic of the Congo</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/2314302"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kinshasa</a>, <a href="https://www.zeitverschiebung.net/cn/city/2593460"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Masina</a>, <a href="https://www.zeitverschiebung.net/cn/city/2314705"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kikwit</a>, <a href="https://www.zeitverschiebung.net/cn/city/2312895"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mbandaka</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2313002"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Matadi</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--lagos">Africa/Lagos</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ng"><span class="flag-icon flag-icon-ng ' \
       'mr-10"></span>Nigeria</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2332459"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lagos</a>, <a href="https://www.zeitverschiebung.net/cn/city/2335204"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kano</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2339354"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ibadan</a>, <a href="https://www.zeitverschiebung.net/cn/city/2335727"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kaduna</a>, <a href="https://www.zeitverschiebung.net/cn/city/2324774"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Port Harcourt</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--libreville">Africa/Libreville</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ga"><span class="flag-icon flag-icon-ga ' \
       'mr-10"></span>Gabon</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2399697"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Libreville</a>, <a href="https://www.zeitverschiebung.net/cn/city/2396518"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Port-Gentil</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2400555"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Franceville</a>, <a href="https://www.zeitverschiebung.net/cn/city/2396646"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Oyem</a>, <a href="https://www.zeitverschiebung.net/cn/city/2398269"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Moanda</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--luanda">Africa/Luanda</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ao"><span class="flag-icon flag-icon-ao ' \
       'mr-10"></span>Angola</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2240449"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Luanda</a>, <a href="https://www.zeitverschiebung.net/cn/city/2239076"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>N’dalatando</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3348313"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Huambo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3347939"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Lobito</a>, <a href="https://www.zeitverschiebung.net/cn/city/3351663"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Benguela</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--malabo">Africa/Malabo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gq"><span class="flag-icon flag-icon-gq ' \
       'mr-10"></span>Equatorial Guinea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2310046"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bata</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2309527"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Malabo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2309332"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ebebiyin</a>, <a href="https://www.zeitverschiebung.net/cn/city/2310547"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Aconibe</a>, <a href="https://www.zeitverschiebung.net/cn/city/2310309"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Añisoc</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--ndjamena">Africa/Ndjamena</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/td"><span class="flag-icon flag-icon-td ' \
       'mr-10"></span>Chad</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2427123"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>N"Djamena</a>, <a href="https://www.zeitverschiebung.net/cn/city/2427455"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Moundou</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2425791"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sagh</a>, <a href="https://www.zeitverschiebung.net/cn/city/245785"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Abéché</a>, <a href="https://www.zeitverschiebung.net/cn/city/2430506"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kelo</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--niamey">Africa/Niamey</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ne"><span class="flag-icon flag-icon-ne ' \
       'mr-10"></span>Niger</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2440485"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Niamey</a>, <a href="https://www.zeitverschiebung.net/cn/city/2437798"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Zinder</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2441291"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Maradi</a>, <a href="https://www.zeitverschiebung.net/cn/city/2448085"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Agadez</a>, <a href="https://www.zeitverschiebung.net/cn/city/2447938"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Alaghsas</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--porto-novo">Africa/Porto-Novo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bj"><span class="flag-icon flag-icon-bj ' \
       'mr-10"></span>Benin</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2394819"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cotonou</a>, <a href="https://www.zeitverschiebung.net/cn/city/2395914"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Abomey-Calavi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2394560"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Djougou</a>, <a href="https://www.zeitverschiebung.net/cn/city/2392087"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Porto-Novo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2392204"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Parakou</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--tunis">Africa/Tunis</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tn"><span class="flag-icon flag-icon-tn ' \
       'mr-10"></span>Tunisia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2464470"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tunis</a>, <a href="https://www.zeitverschiebung.net/cn/city/2467454"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sfax</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2464915"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sousse</a>, <a href="https://www.zeitverschiebung.net/cn/city/2468925"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Midoun</a>, <a href="https://www.zeitverschiebung.net/cn/city/2473449"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kairouan</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/arctic--longyearbyen">Arctic/Longyearbyen</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sj"><span class="flag-icon flag-icon-sj ' \
       'mr-10"></span>Svalbard and Jan Mayen</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/2729907"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Longyearbyen</a>, <a href="https://www.zeitverschiebung.net/cn/city/7535941"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Olonkinbyen</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--amsterdam">Europe/Amsterdam</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nl"><span class="flag-icon flag-icon-nl ' \
       'mr-10"></span>Netherlands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2759794"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Amsterdam</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2747891"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Rotterdam</a>, <a href="https://www.zeitverschiebung.net/cn/city/2747373"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>The Hague</a>, <a href="https://www.zeitverschiebung.net/cn/city/2745912"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Utrecht</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2756253"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Eindhoven</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--andorra">Europe/Andorra</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ad"><span class="flag-icon flag-icon-ad ' \
       'mr-10"></span>Andorra</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3041563"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Andorra la Vella</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3040051"><i class="fa fa-map-marker pr-5 pl-5"></i>les ' \
       'Escaldes</a>, <a href="https://www.zeitverschiebung.net/cn/city/3040686"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Encamp</a>, <a href="https://www.zeitverschiebung.net/cn/city/3039163"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sant Julià de Lòria</a>, <a href="https://www.zeitverschiebung.net/cn/city/3040132"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>la Massana</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--belgrade">Europe/Belgrade</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/rs"><span class="flag-icon flag-icon-rs ' \
       'mr-10"></span>Serbia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/792680"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Belgrade</a>, <a href="https://www.zeitverschiebung.net/cn/city/786714"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pristina</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/787657"><i class="fa fa-map-marker pr-5 pl-5"></i>Niš</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3194360"><i class="fa fa-map-marker pr-5 pl-5"></i>Novi ' \
       'Sad</a>, <a href="https://www.zeitverschiebung.net/cn/city/786712"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Prizren</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--berlin">Europe/Berlin</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/de"><span class="flag-icon flag-icon-de ' \
       'mr-10"></span>Germany</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2950159"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Berlin</a>, <a href="https://www.zeitverschiebung.net/cn/city/2911298"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Hamburg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2867714"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>München</a>, <a href="https://www.zeitverschiebung.net/cn/city/2886242"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Köln</a>, <a href="https://www.zeitverschiebung.net/cn/city/2925533"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Frankfurt am Main</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--bratislava">Europe/Bratislava</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sk"><span class="flag-icon flag-icon-sk ' \
       'mr-10"></span>Slovakia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3060972"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bratislava</a>, <a href="https://www.zeitverschiebung.net/cn/city/724443"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Košice</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/723819"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Prešov</a>, <a href="https://www.zeitverschiebung.net/cn/city/3058531"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nitra</a>, <a href="https://www.zeitverschiebung.net/cn/city/3056508"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Žilina</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--brussels">Europe/Brussels</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/be"><span class="flag-icon flag-icon-be ' \
       'mr-10"></span>Belgium</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2800866"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Brussels</a>, <a href="https://www.zeitverschiebung.net/cn/city/2803138"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Antwerpen</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2797656"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Gent</a>, <a href="https://www.zeitverschiebung.net/cn/city/2800481"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Charleroi</a>, <a href="https://www.zeitverschiebung.net/cn/city/2792413"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Liège</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--budapest">Europe/Budapest</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/hu"><span class="flag-icon flag-icon-hu ' \
       'mr-10"></span>Hungary</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3054643"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Budapest</a>, <a href="https://www.zeitverschiebung.net/cn/city/721472"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Debrecen</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/717582"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Miskolc</a>, <a href="https://www.zeitverschiebung.net/cn/city/715429"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Szeged</a>, <a href="https://www.zeitverschiebung.net/cn/city/3046526"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pécs</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--copenhagen">Europe/Copenhagen</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/dk"><span class="flag-icon flag-icon-dk ' \
       'mr-10"></span>Denmark</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2618425"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Copenhagen</a>, <a href="https://www.zeitverschiebung.net/cn/city/2624652"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Århus</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2615876"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Odense</a>, <a href="https://www.zeitverschiebung.net/cn/city/2624886"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Aalborg</a>, <a href="https://www.zeitverschiebung.net/cn/city/2621942"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Frederiksberg</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--dublin">Europe/Dublin</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ie"><span class="flag-icon flag-icon-ie ' \
       'mr-10"></span>Ireland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2964574"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dublin</a>, <a href="https://www.zeitverschiebung.net/cn/city/2965140"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Cork</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2964506"><i class="fa fa-map-marker pr-5 pl-5"></i>Dún ' \
       'Laoghaire</a>, <a href="https://www.zeitverschiebung.net/cn/city/2962943"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Luimneach</a>, <a href="https://www.zeitverschiebung.net/cn/city/2964180"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gaillimh</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--gibraltar">Europe/Gibraltar</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gi"><span class="flag-icon flag-icon-gi ' \
       'mr-10"></span>Gibraltar</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2411585"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gibraltar</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--ljubljana">Europe/Ljubljana</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/si"><span class="flag-icon flag-icon-si ' \
       'mr-10"></span>Slovenia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3196359"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ljubljana</a>, <a href="https://www.zeitverschiebung.net/cn/city/3195506"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maribor</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3202781"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Celje</a>, <a href="https://www.zeitverschiebung.net/cn/city/3197378"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kranj</a>, <a href="https://www.zeitverschiebung.net/cn/city/3189075"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Velenje</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--luxembourg">Europe/Luxembourg</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lu"><span class="flag-icon flag-icon-lu ' \
       'mr-10"></span>Luxembourg</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2960316"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Luxembourg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2960596"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Esch-sur-Alzette</a>, <a href="https://www.zeitverschiebung.net/cn/city/2960634"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dudelange</a>, <a href="https://www.zeitverschiebung.net/cn/city/2960102"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Schifflange</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2960777"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bettembourg</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--madrid">Europe/Madrid</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/es"><span class="flag-icon flag-icon-es ' \
       'mr-10"></span>Spain</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3117735"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Madrid</a>, <a href="https://www.zeitverschiebung.net/cn/city/3128760"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Barcelona</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2509954"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Valencia</a>, <a href="https://www.zeitverschiebung.net/cn/city/2510911"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sevilla</a>, <a href="https://www.zeitverschiebung.net/cn/city/3104324"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zaragoza</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--malta">Europe/Malta</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mt"><span class="flag-icon flag-icon-mt ' \
       'mr-10"></span>Malta</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2563191"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Birkirkara</a>, <a href="https://www.zeitverschiebung.net/cn/city/2562629"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Qormi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2562704"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mosta</a>, <a href="https://www.zeitverschiebung.net/cn/city/2562266"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Żabbar</a>, <a href="https://www.zeitverschiebung.net/cn/city/2562541"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>San Pawl il-Baħar</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--monaco">Europe/Monaco</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mc"><span class="flag-icon flag-icon-mc ' \
       'mr-10"></span>Monaco</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2993458"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Monaco</a>, <a href="https://www.zeitverschiebung.net/cn/city/2992741"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Monte-Carlo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3009937"><i class="fa fa-map-marker pr-5 pl-5"></i>La ' \
       'Condamine</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--oslo">Europe/Oslo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/no"><span class="flag-icon flag-icon-no ' \
       'mr-10"></span>Norway</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3143244"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Oslo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3161732"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bergen</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3133880"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Trondheim</a>, <a href="https://www.zeitverschiebung.net/cn/city/3137115"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Stavanger</a>, <a href="https://www.zeitverschiebung.net/cn/city/3159016"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Drammen</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--paris">Europe/Paris</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fr"><span class="flag-icon flag-icon-fr ' \
       'mr-10"></span>France</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2988507"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Paris</a>, <a href="https://www.zeitverschiebung.net/cn/city/2995469"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Marseille</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2996944"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Lyon</a>, <a href="https://www.zeitverschiebung.net/cn/city/2972315"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Toulouse</a>, <a href="https://www.zeitverschiebung.net/cn/city/2990440"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nice</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--podgorica">Europe/Podgorica</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/me"><span class="flag-icon flag-icon-me ' \
       'mr-10"></span>Montenegro</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3193044"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Podgorica</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3194494"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nikšić</a>, <a href="https://www.zeitverschiebung.net/cn/city/3199394"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Herceg-Novi</a>, <a href="https://www.zeitverschiebung.net/cn/city/3193161"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pljevlja</a>, <a href="https://www.zeitverschiebung.net/cn/city/3203106"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Budva</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--prague">Europe/Prague</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cz"><span class="flag-icon flag-icon-cz mr-10"></span>Czech ' \
       'Republic</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3067696"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Prague</a>, <a href="https://www.zeitverschiebung.net/cn/city/3078610"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Brno</a>, <a href="https://www.zeitverschiebung.net/cn/city/3068799"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ostrava</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3068160"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Pilsen</a>, <a href="https://www.zeitverschiebung.net/cn/city/3069011"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Olomouc</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--rome">Europe/Rome</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/it"><span class="flag-icon flag-icon-it ' \
       'mr-10"></span>Italy</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3169070"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rome</a>, <a href="https://www.zeitverschiebung.net/cn/city/3173435"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Milano</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3172394"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Napoli</a>, <a href="https://www.zeitverschiebung.net/cn/city/3165524"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Turin</a>, <a href="https://www.zeitverschiebung.net/cn/city/2523920"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Palermo</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--san_marino">Europe/San_Marino</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sm"><span class="flag-icon flag-icon-sm mr-10"></span>San ' \
       'Marino</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3166645"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Serravalle</a>, <a href="https://www.zeitverschiebung.net/cn/city/3181793"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Borgo Maggiore</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3168070"><i class="fa fa-map-marker pr-5 pl-5"></i>San ' \
       'Marino</a>, <a href="https://www.zeitverschiebung.net/cn/city/3177542"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Domagnano</a>, <a href="https://www.zeitverschiebung.net/cn/city/3176966"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Fiorentino</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--sarajevo">Europe/Sarajevo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ba"><span class="flag-icon flag-icon-ba ' \
       'mr-10"></span>Bosnia and Herzegovina</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/3191281"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sarajevo</a>, <a href="https://www.zeitverschiebung.net/cn/city/3204541"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Banja Luka</a>, <a href="https://www.zeitverschiebung.net/cn/city/3186573"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zenica</a>, <a href="https://www.zeitverschiebung.net/cn/city/3188582"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tuzla</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3194828"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mostar</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--skopje">Europe/Skopje</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mk"><span class="flag-icon flag-icon-mk ' \
       'mr-10"></span>Macedonia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/785842"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Skopje</a>, <a href="https://www.zeitverschiebung.net/cn/city/792578"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bitola</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/788886"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kumanovo</a>, <a href="https://www.zeitverschiebung.net/cn/city/786735"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Prilep</a>, <a href="https://www.zeitverschiebung.net/cn/city/785082"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tetovo</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--stockholm">Europe/Stockholm</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/se"><span class="flag-icon flag-icon-se ' \
       'mr-10"></span>Sweden</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2673730"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Stockholm</a>, <a href="https://www.zeitverschiebung.net/cn/city/2711537"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Göteborg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2692969"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Malmö</a>, <a href="https://www.zeitverschiebung.net/cn/city/2666199"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Uppsala</a>, <a href="https://www.zeitverschiebung.net/cn/city/2664454"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Västerås</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--tirane">Europe/Tirane</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/al"><span class="flag-icon flag-icon-al ' \
       'mr-10"></span>Albania</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3183875"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tirana</a>, <a href="https://www.zeitverschiebung.net/cn/city/3185728"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Durrës</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/783263"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Elbasan</a>, <a href="https://www.zeitverschiebung.net/cn/city/3183719"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Vlorë</a>, <a href="https://www.zeitverschiebung.net/cn/city/3184081"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Shkodër</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--vaduz">Europe/Vaduz</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/li"><span class="flag-icon flag-icon-li ' \
       'mr-10"></span>Liechtenstein</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3042041"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Schaan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3042030"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Vaduz</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042035"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Triesen</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042073"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Balzers</a>, <a href="https://www.zeitverschiebung.net/cn/city/3042068"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Eschen</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--vatican">Europe/Vatican</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/va"><span class="flag-icon flag-icon-va ' \
       'mr-10"></span>Vatican</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6691831"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vatican City</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--vienna">Europe/Vienna</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/at"><span class="flag-icon flag-icon-at ' \
       'mr-10"></span>Austria</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2761369"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vienna</a>, <a href="https://www.zeitverschiebung.net/cn/city/2778067"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Graz</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2772400"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Linz</a>, <a href="https://www.zeitverschiebung.net/cn/city/2766824"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Salzburg</a>, <a href="https://www.zeitverschiebung.net/cn/city/2775220"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Innsbruck</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--warsaw">Europe/Warsaw</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pl"><span class="flag-icon flag-icon-pl ' \
       'mr-10"></span>Poland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/756135"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Warsaw</a>, <a href="https://www.zeitverschiebung.net/cn/city/3093133"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Łódź</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3094802"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kraków</a>, <a href="https://www.zeitverschiebung.net/cn/city/3081368"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Wrocław</a>, <a href="https://www.zeitverschiebung.net/cn/city/3088171"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Poznań</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--zagreb">Europe/Zagreb</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/hr"><span class="flag-icon flag-icon-hr ' \
       'mr-10"></span>Croatia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/6618983"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zagreb - Centar</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3186886"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Zagreb</a>, <a href="https://www.zeitverschiebung.net/cn/city/3190261"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Split</a>, <a href="https://www.zeitverschiebung.net/cn/city/3191648"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rijeka</a>, <a href="https://www.zeitverschiebung.net/cn/city/3193935"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Osijek</a> </td> </tr> <tr> <td><strong>UTC+1</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--zurich">Europe/Zurich</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ch"><span class="flag-icon flag-icon-ch ' \
       'mr-10"></span>Switzerland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2657896"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Zürich</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2660646"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Genève</a>, <a href="https://www.zeitverschiebung.net/cn/city/2661604"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Basel</a>, <a href="https://www.zeitverschiebung.net/cn/city/2661552"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bern</a>, <a href="https://www.zeitverschiebung.net/cn/city/2659994"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lausanne</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--blantyre">Africa/Blantyre</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mw"><span class="flag-icon flag-icon-mw ' \
       'mr-10"></span>Malawi</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/927967"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lilongwe</a>, <a href="https://www.zeitverschiebung.net/cn/city/931755"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Blantyre</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/925475"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mzuzu</a>, <a href="https://www.zeitverschiebung.net/cn/city/923295"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Zomba</a>, <a href="https://www.zeitverschiebung.net/cn/city/928534"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kasungu</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--bujumbura">Africa/Bujumbura</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bi"><span class="flag-icon flag-icon-bi ' \
       'mr-10"></span>Burundi</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/425378"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bujumbura</a>, <a href="https://www.zeitverschiebung.net/cn/city/431748"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Muyinga</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/426700"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ruyigi</a>, <a href="https://www.zeitverschiebung.net/cn/city/426272"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Gitega</a>, <a href="https://www.zeitverschiebung.net/cn/city/430569"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ngozi</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--cairo">Africa/Cairo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/eg"><span class="flag-icon flag-icon-eg ' \
       'mr-10"></span>Egypt</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/360630"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cairo</a>, <a href="https://www.zeitverschiebung.net/cn/city/361058"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Alexandria</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/360995"><i class="fa fa-map-marker pr-5 pl-5"></i>Al ' \
       'Jīzah</a>, <a href="https://www.zeitverschiebung.net/cn/city/358619"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Port Said</a>, <a href="https://www.zeitverschiebung.net/cn/city/359796"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Suez</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--gaborone">Africa/Gaborone</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bw"><span class="flag-icon flag-icon-bw ' \
       'mr-10"></span>Botswana</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/933773"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gaborone</a>, <a href="https://www.zeitverschiebung.net/cn/city/933778"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Francistown</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/933305"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Molepolole</a>, <a href="https://www.zeitverschiebung.net/cn/city/933099"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Selebi-Phikwe</a>, <a href="https://www.zeitverschiebung.net/cn/city/933366"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maun</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--harare">Africa/Harare</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/zw"><span class="flag-icon flag-icon-zw ' \
       'mr-10"></span>Zimbabwe</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/890299"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Harare</a>, <a href="https://www.zeitverschiebung.net/cn/city/894701"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bulawayo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1106542"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Chitungwiza</a>, <a href="https://www.zeitverschiebung.net/cn/city/884979"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mutare</a>, <a href="https://www.zeitverschiebung.net/cn/city/890422"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gweru</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--johannesburg">Africa/Johannesburg</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/za"><span class="flag-icon flag-icon-za mr-10"></span>South ' \
       'Africa</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3369157"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Cape Town</a>, <a href="https://www.zeitverschiebung.net/cn/city/1007311"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Durban</a>, <a href="https://www.zeitverschiebung.net/cn/city/993800"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Johannesburg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/953781"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Soweto</a>, <a href="https://www.zeitverschiebung.net/cn/city/964137"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Pretoria</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--khartoum">Africa/Khartoum</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sd"><span class="flag-icon flag-icon-sd ' \
       'mr-10"></span>Sudan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/379252"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Khartoum</a>, <a href="https://www.zeitverschiebung.net/cn/city/365137"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Omdurman</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/377039"><i class="fa fa-map-marker pr-5 pl-5"></i>Port ' \
       'Sudan</a>, <a href="https://www.zeitverschiebung.net/cn/city/372753"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kassala</a>, <a href="https://www.zeitverschiebung.net/cn/city/379003"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>El Obeid</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--kigali">Africa/Kigali</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/rw"><span class="flag-icon flag-icon-rw ' \
       'mr-10"></span>Rwanda</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/202061"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kigali</a>, <a href="https://www.zeitverschiebung.net/cn/city/203112"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Butare</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/202217"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Gitarama</a>, <a href="https://www.zeitverschiebung.net/cn/city/201521"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Musanze</a>, <a href="https://www.zeitverschiebung.net/cn/city/202905"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gisenyi</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--lubumbashi">Africa/Lubumbashi</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cd"><span class="flag-icon flag-icon-cd ' \
       'mr-10"></span>Democratic Republic of the Congo</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/922704"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Lubumbashi</a>, <a href="https://www.zeitverschiebung.net/cn/city/209228"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mbuji-Mayi</a>, <a href="https://www.zeitverschiebung.net/cn/city/212730"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kisangani</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/214481"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kananga</a>, <a href="https://www.zeitverschiebung.net/cn/city/922741"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Likasi</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--lusaka">Africa/Lusaka</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/zm"><span class="flag-icon flag-icon-zm ' \
       'mr-10"></span>Zambia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/909137"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lusaka</a>, <a href="https://www.zeitverschiebung.net/cn/city/911148"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kitwe</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/901344"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ndola</a>, <a href="https://www.zeitverschiebung.net/cn/city/916095"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kabwe</a>, <a href="https://www.zeitverschiebung.net/cn/city/919009"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chingola</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--maputo">Africa/Maputo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mz"><span class="flag-icon flag-icon-mz ' \
       'mr-10"></span>Mozambique</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1040652"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maputo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1039854"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Matola</a>, <a href="https://www.zeitverschiebung.net/cn/city/1052373"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Beira</a>, <a href="https://www.zeitverschiebung.net/cn/city/1033356"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nampula</a>, <a href="https://www.zeitverschiebung.net/cn/city/1049261"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chimoio</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--maseru">Africa/Maseru</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ls"><span class="flag-icon flag-icon-ls ' \
       'mr-10"></span>Lesotho</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/932505"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Maseru</a>, <a href="https://www.zeitverschiebung.net/cn/city/932614"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mafeteng</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/932698"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Leribe</a>, <a href="https://www.zeitverschiebung.net/cn/city/932521"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Maputsoe</a>, <a href="https://www.zeitverschiebung.net/cn/city/932438"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mohale’s Hoek</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--mbabane">Africa/Mbabane</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sz"><span class="flag-icon flag-icon-sz ' \
       'mr-10"></span>Swaziland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/934995"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Manzini</a>, <a href="https://www.zeitverschiebung.net/cn/city/934985"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mbabane</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/935113"><i class="fa fa-map-marker pr-5 pl-5"></i>Big ' \
       'Bend</a>, <a href="https://www.zeitverschiebung.net/cn/city/935005"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Malkerns</a>, <a href="https://www.zeitverschiebung.net/cn/city/934966"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mhlume</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--tripoli">Africa/Tripoli</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ly"><span class="flag-icon flag-icon-ly ' \
       'mr-10"></span>Libya</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2210247"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tripoli</a>, <a href="https://www.zeitverschiebung.net/cn/city/88319"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Benghazi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2214846"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mişrātah</a>, <a href="https://www.zeitverschiebung.net/cn/city/2210221"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tarhuna</a>, <a href="https://www.zeitverschiebung.net/cn/city/2219905"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Al Khums</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--windhoek">Africa/Windhoek</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/na"><span class="flag-icon flag-icon-na ' \
       'mr-10"></span>Namibia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3352136"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Windhoek</a>, <a href="https://www.zeitverschiebung.net/cn/city/3353383"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rundu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/3359638"><i class="fa fa-map-marker pr-5 pl-5"></i>Walvis ' \
       'Bay</a>, <a href="https://www.zeitverschiebung.net/cn/city/3354021"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Oshakati</a>, <a href="https://www.zeitverschiebung.net/cn/city/3352844"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Swakopmund</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--amman">Asia/Amman</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/jo"><span class="flag-icon flag-icon-jo ' \
       'mr-10"></span>Jordan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/250441"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Amman</a>, <a href="https://www.zeitverschiebung.net/cn/city/250090"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Zarqa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/248946"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Irbid</a>, <a href="https://www.zeitverschiebung.net/cn/city/7838895"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Russeifa</a>, <a href="https://www.zeitverschiebung.net/cn/city/246013"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Wādī as Sīr</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--beirut">Asia/Beirut</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lb"><span class="flag-icon flag-icon-lb ' \
       'mr-10"></span>Lebanon</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/276781"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Beirut</a>, <a href="https://www.zeitverschiebung.net/cn/city/268743"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ra’s Bayrūt</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/266826"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tripoli</a>, <a href="https://www.zeitverschiebung.net/cn/city/268064"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sidon</a>, <a href="https://www.zeitverschiebung.net/cn/city/267008"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tyre</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--damascus">Asia/Damascus</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sy"><span class="flag-icon flag-icon-sy ' \
       'mr-10"></span>Syria</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/170063"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Aleppo</a>, <a href="https://www.zeitverschiebung.net/cn/city/170654"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Damascus</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/169577"><i class="fa fa-map-marker pr-5 pl-5"></i>Homs</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/170017"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ḩamāh</a>, <a href="https://www.zeitverschiebung.net/cn/city/173576"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Latakia</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--famagusta">Asia/Famagusta</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cy"><span class="flag-icon flag-icon-cy ' \
       'mr-10"></span>Cyprus</a></td> <td> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--gaza">Asia/Gaza</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ps"><span class="flag-icon flag-icon-ps ' \
       'mr-10"></span>Palestinian Territory</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/281133"><i class="fa fa-map-marker pr-5 pl-5"></i>Gaza</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/281124"><i class="fa fa-map-marker pr-5 pl-5"></i>Khān ' \
       'Yūnis</a>, <a href="https://www.zeitverschiebung.net/cn/city/281129"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Jabālyā</a>, <a href="https://www.zeitverschiebung.net/cn/city/281102"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Rafaḩ</a>, <a href="https://www.zeitverschiebung.net/cn/city/281141"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dayr al Balaḩ</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--hebron">Asia/Hebron</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ps"><span class="flag-icon flag-icon-ps ' \
       'mr-10"></span>Palestinian Territory</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/7303419"><i class="fa fa-map-marker pr-5 pl-5"></i>East ' \
       'Jerusalem</a>, <a href="https://www.zeitverschiebung.net/cn/city/285066"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hebron</a>, <a href="https://www.zeitverschiebung.net/cn/city/282615"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nablus</a>, <a href="https://www.zeitverschiebung.net/cn/city/281577"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ţūlkarm</a>, <a href="https://www.zeitverschiebung.net/cn/city/282457"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Qalqīlyah</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--jerusalem">Asia/Jerusalem</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/il"><span class="flag-icon flag-icon-il ' \
       'mr-10"></span>Israel</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/281184"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Jerusalem</a>, <a href="https://www.zeitverschiebung.net/cn/city/7498240"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>West Jerusalem</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/294801"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Haifa</a>, <a href="https://www.zeitverschiebung.net/cn/city/293397"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tel Aviv</a>, <a href="https://www.zeitverschiebung.net/cn/city/295629"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ashdod</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--nicosia">Asia/Nicosia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cy"><span class="flag-icon flag-icon-cy ' \
       'mr-10"></span>Cyprus</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/146268"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nicosia</a>, <a href="https://www.zeitverschiebung.net/cn/city/146384"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Limassol</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/146400"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Larnaca</a>, <a href="https://www.zeitverschiebung.net/cn/city/146617"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Famagusta</a>, <a href="https://www.zeitverschiebung.net/cn/city/146214"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Paphos</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--athens">Europe/Athens</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gr"><span class="flag-icon flag-icon-gr ' \
       'mr-10"></span>Greece</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/264371"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Athens</a>, <a href="https://www.zeitverschiebung.net/cn/city/734077"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Thessaloníki</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/255683"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Pátra</a>, <a href="https://www.zeitverschiebung.net/cn/city/255274"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Piraeus</a>, <a href="https://www.zeitverschiebung.net/cn/city/258576"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lárisa</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--bucharest">Europe/Bucharest</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ro"><span class="flag-icon flag-icon-ro ' \
       'mr-10"></span>Romania</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/683506"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bucharest</a>, <a href="https://www.zeitverschiebung.net/cn/city/11048319"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sector 3</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/11048323"><i class="fa fa-map-marker pr-5 pl-5"></i>Sector ' \
       '6</a>, <a href="https://www.zeitverschiebung.net/cn/city/11048318"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sector 2</a>, <a href="https://www.zeitverschiebung.net/cn/city/675810"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Iaşi</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--chisinau">Europe/Chisinau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/md"><span class="flag-icon flag-icon-md ' \
       'mr-10"></span>Moldova</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/618426"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chişinău</a>, <a href="https://www.zeitverschiebung.net/cn/city/617239"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tiraspolul</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/618605"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bălţi</a>, <a href="https://www.zeitverschiebung.net/cn/city/618577"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bender</a>, <a href="https://www.zeitverschiebung.net/cn/city/617486"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rîbniţa</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--helsinki">Europe/Helsinki</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fi"><span class="flag-icon flag-icon-fi ' \
       'mr-10"></span>Finland</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/658225"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Helsinki</a>, <a href="https://www.zeitverschiebung.net/cn/city/660158"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Espoo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/634963"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tampere</a>, <a href="https://www.zeitverschiebung.net/cn/city/632453"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Vantaa</a>, <a href="https://www.zeitverschiebung.net/cn/city/633679"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Turku</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--kaliningrad">Europe/Kaliningrad</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/554234"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kaliningrad</a>, <a href="https://www.zeitverschiebung.net/cn/city/568595"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chernyakhovsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/490068"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sovetsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2609906"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Baltiysk</a>, <a href="https://www.zeitverschiebung.net/cn/city/557882"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Gusev</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--kiev">Europe/Kiev</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ua"><span class="flag-icon flag-icon-ua ' \
       'mr-10"></span>Ukraine</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/703448"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kiev</a>, <a href="https://www.zeitverschiebung.net/cn/city/706483"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kharkiv</a>, <a href="https://www.zeitverschiebung.net/cn/city/709930"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dnipropetrovsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/709717"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Donetsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/698740"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Odessa</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--mariehamn">Europe/Mariehamn</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ax"><span class="flag-icon flag-icon-ax mr-10"></span>Aland ' \
       'Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/3041732"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mariehamn</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--riga">Europe/Riga</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lv"><span class="flag-icon flag-icon-lv ' \
       'mr-10"></span>Latvia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/456172"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Riga</a>, <a href="https://www.zeitverschiebung.net/cn/city/460413"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Daugavpils</a>, <a href="https://www.zeitverschiebung.net/cn/city/454432"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Vec-Liepāja</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/457954"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Liepāja</a>, <a href="https://www.zeitverschiebung.net/cn/city/459279"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Jelgava</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--sofia">Europe/Sofia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bg"><span class="flag-icon flag-icon-bg ' \
       'mr-10"></span>Bulgaria</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/727011"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sofia</a>, <a href="https://www.zeitverschiebung.net/cn/city/728193"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Plovdiv</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/726050"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Varna</a>, <a href="https://www.zeitverschiebung.net/cn/city/732770"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Burgas</a>, <a href="https://www.zeitverschiebung.net/cn/city/727523"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ruse</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--tallinn">Europe/Tallinn</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ee"><span class="flag-icon flag-icon-ee ' \
       'mr-10"></span>Estonia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/588409"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tallinn</a>, <a href="https://www.zeitverschiebung.net/cn/city/588335"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tartu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/590031"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Narva</a>, <a href="https://www.zeitverschiebung.net/cn/city/591260"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kohtla-Järve</a>, <a href="https://www.zeitverschiebung.net/cn/city/589580"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pärnu</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--uzhgorod">Europe/Uzhgorod</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ua"><span class="flag-icon flag-icon-ua ' \
       'mr-10"></span>Ukraine</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/690548"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Uzhhorod</a>, <a href="https://www.zeitverschiebung.net/cn/city/700646"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mukacheve</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/706165"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Khust</a>, <a href="https://www.zeitverschiebung.net/cn/city/688746"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Vynohradiv</a>, <a href="https://www.zeitverschiebung.net/cn/city/712423"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Berehove</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--vilnius">Europe/Vilnius</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lt"><span class="flag-icon flag-icon-lt ' \
       'mr-10"></span>Lithuania</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/593116"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vilnius</a>, <a href="https://www.zeitverschiebung.net/cn/city/598316"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kaunas</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/598098"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Klaipėda</a>, <a href="https://www.zeitverschiebung.net/cn/city/594739"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Šiauliai</a>, <a href="https://www.zeitverschiebung.net/cn/city/596128"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Panevėžys</a> </td> </tr> <tr> <td><strong>UTC+2</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--zaporozhye">Europe/Zaporozhye</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ua"><span class="flag-icon flag-icon-ua ' \
       'mr-10"></span>Ukraine</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/687700"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zaporizhzhya</a>, <a href="https://www.zeitverschiebung.net/cn/city/702658"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Luhansk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/701404"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Melitopol’</a>, <a href="https://www.zeitverschiebung.net/cn/city/691999"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Syevyerodonets’k</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/712451"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Berdyans’k</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--addis_ababa">Africa/Addis_Ababa</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/et"><span class="flag-icon flag-icon-et ' \
       'mr-10"></span>Ethiopia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/344979"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Addis Ababa</a>, <a href="https://www.zeitverschiebung.net/cn/city/338832"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dire Dawa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/331180"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mekele</a>, <a href="https://www.zeitverschiebung.net/cn/city/330186"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nazrēt</a>, <a href="https://www.zeitverschiebung.net/cn/city/342884"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bahir Dar</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--asmara">Africa/Asmara</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/er"><span class="flag-icon flag-icon-er ' \
       'mr-10"></span>Eritrea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/343300"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Asmara</a>, <a href="https://www.zeitverschiebung.net/cn/city/333287"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Keren</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/330546"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Massawa</a>, <a href="https://www.zeitverschiebung.net/cn/city/343386"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Assab</a>, <a href="https://www.zeitverschiebung.net/cn/city/344901"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mendefera</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--dar_es_salaam">Africa/Dar_es_Salaam</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/tz"><span class="flag-icon flag-icon-tz ' \
       'mr-10"></span>Tanzania</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/160263"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dar es Salaam</a>, <a href="https://www.zeitverschiebung.net/cn/city/152224"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mwanza</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/148730"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Zanzibar</a>, <a href="https://www.zeitverschiebung.net/cn/city/161325"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Arusha</a>, <a href="https://www.zeitverschiebung.net/cn/city/154380"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mbeya</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--djibouti">Africa/Djibouti</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/dj"><span class="flag-icon flag-icon-dj ' \
       'mr-10"></span>Djibouti</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/223817"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Djibouti</a>, <a href="https://www.zeitverschiebung.net/cn/city/224152"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ḏânan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/225284"><i class="fa fa-map-marker pr-5 pl-5"></i>"Ali ' \
       'Sabieh</a>, <a href="https://www.zeitverschiebung.net/cn/city/220782"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tadjoura</a>, <a href="https://www.zeitverschiebung.net/cn/city/221527"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Obock</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--juba">Africa/Juba</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ss"><span class="flag-icon flag-icon-ss mr-10"></span>South ' \
       'Sudan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/373303"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Juba</a>, <a href="https://www.zeitverschiebung.net/cn/city/370737"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Malakal</a>, <a href="https://www.zeitverschiebung.net/cn/city/363885"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Wau</a>, <a href="https://www.zeitverschiebung.net/cn/city/375495"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Pajok</a>, <a href="https://www.zeitverschiebung.net/cn/city/363619"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yei</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--kampala">Africa/Kampala</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ug"><span class="flag-icon flag-icon-ug ' \
       'mr-10"></span>Uganda</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/232422"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kampala</a>, <a href="https://www.zeitverschiebung.net/cn/city/233346"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gulu</a>, <a href="https://www.zeitverschiebung.net/cn/city/230166"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lira</a>, <a href="https://www.zeitverschiebung.net/cn/city/229268"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mbarara</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/233114"><i class="fa fa-map-marker pr-5 pl-5"></i>Jinja</a> ' \
       '</td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--mogadishu">Africa/Mogadishu</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/so"><span class="flag-icon flag-icon-so ' \
       'mr-10"></span>Somalia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/53654"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mogadishu</a>, <a href="https://www.zeitverschiebung.net/cn/city/57289"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Hargeysa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/64435"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Berbera</a>, <a href="https://www.zeitverschiebung.net/cn/city/55671"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kismayo</a>, <a href="https://www.zeitverschiebung.net/cn/city/54225"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Marka</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/africa--nairobi">Africa/Nairobi</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ke"><span class="flag-icon flag-icon-ke ' \
       'mr-10"></span>Kenya</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/184745"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nairobi</a>, <a href="https://www.zeitverschiebung.net/cn/city/186301"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mombasa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/184622"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nakuru</a>, <a href="https://www.zeitverschiebung.net/cn/city/198629"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Eldoret</a>, <a href="https://www.zeitverschiebung.net/cn/city/191245"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kisumu</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--syowa">Antarctica/Syowa</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--aden">Asia/Aden</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ye"><span class="flag-icon flag-icon-ye ' \
       'mr-10"></span>Yemen</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/71137"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sanaa</a>, <a href="https://www.zeitverschiebung.net/cn/city/79415"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Al Ḩudaydah</a>, <a href="https://www.zeitverschiebung.net/cn/city/70225"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ta‘izz</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/415189"><i class="fa fa-map-marker pr-5 pl-5"></i>Aden</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/78754"><i class="fa fa-map-marker pr-5 pl-5"></i>Al ' \
       'Mukallā</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--baghdad">Asia/Baghdad</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/iq"><span class="flag-icon flag-icon-iq ' \
       'mr-10"></span>Iraq</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/98182"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Baghdad</a>, <a href="https://www.zeitverschiebung.net/cn/city/99532"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Basrah</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/99071"><i class="fa fa-map-marker pr-5 pl-5"></i>Al Mawşil ' \
       'al Jadīdah</a>, <a href="https://www.zeitverschiebung.net/cn/city/388349"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Al Başrah al Qadīmah</a>, <a href="https://www.zeitverschiebung.net/cn/city/99072"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mosul</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--bahrain">Asia/Bahrain</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bh"><span class="flag-icon flag-icon-bh ' \
       'mr-10"></span>Bahrain</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/290340"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Manama</a>, <a href="https://www.zeitverschiebung.net/cn/city/290332"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Al Muharraq</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/385038"><i class="fa fa-map-marker pr-5 pl-5"></i>Ar ' \
       'Rifā‘</a>, <a href="https://www.zeitverschiebung.net/cn/city/290269"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Dār Kulayb</a>, <a href="https://www.zeitverschiebung.net/cn/city/290247"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Madīnat Ḩamad</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--kuwait">Asia/Kuwait</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kw"><span class="flag-icon flag-icon-kw ' \
       'mr-10"></span>Kuwait</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/285839"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Al Aḩmadī</a>, <a href="https://www.zeitverschiebung.net/cn/city/285629"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ḩawallī</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/285704"><i class="fa fa-map-marker pr-5 pl-5"></i>As ' \
       'Sālimīyah</a>, <a href="https://www.zeitverschiebung.net/cn/city/412800"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Şabāḩ as Sālim</a>, <a href="https://www.zeitverschiebung.net/cn/city/285815"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Al Farwānīyah</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--qatar">Asia/Qatar</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/qa"><span class="flag-icon flag-icon-qa ' \
       'mr-10"></span>Qatar</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/290030"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Doha</a>, <a href="https://www.zeitverschiebung.net/cn/city/289888"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ar Rayyān</a>, <a href="https://www.zeitverschiebung.net/cn/city/289523"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Umm Şalāl Muḩammad</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/289915"><i class="fa fa-map-marker pr-5 pl-5"></i>Al ' \
       'Wakrah</a>, <a href="https://www.zeitverschiebung.net/cn/city/289962"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Al Khawr</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--riyadh">Asia/Riyadh</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sa"><span class="flag-icon flag-icon-sa mr-10"></span>Saudi ' \
       'Arabia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/108410"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Riyadh</a>, <a href="https://www.zeitverschiebung.net/cn/city/105343"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Jeddah</a>, <a href="https://www.zeitverschiebung.net/cn/city/104515"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mecca</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/109223"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Medina</a>, <a href="https://www.zeitverschiebung.net/cn/city/101760"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sulţānah</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--istanbul">Europe/Istanbul</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tr"><span class="flag-icon flag-icon-tr ' \
       'mr-10"></span>Turkey</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/745044"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>İstanbul</a>, <a href="https://www.zeitverschiebung.net/cn/city/323786"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ankara</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/311046"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>İzmir</a>, <a href="https://www.zeitverschiebung.net/cn/city/750269"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bursa</a>, <a href="https://www.zeitverschiebung.net/cn/city/325363"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Adana</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--kirov">Europe/Kirov</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--minsk">Europe/Minsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/by"><span class="flag-icon flag-icon-by ' \
       'mr-10"></span>Belarus</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/625144"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Minsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/627907"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gomel</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/625665"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mahilyow</a>, <a href="https://www.zeitverschiebung.net/cn/city/620127"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Vitebsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/627904"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hrodna</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--moscow">Europe/Moscow</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/524901"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Moscow</a>, <a href="https://www.zeitverschiebung.net/cn/city/498817"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saint Petersburg</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/520555"><i class="fa fa-map-marker pr-5 pl-5"></i>Nizhniy ' \
       'Novgorod</a>, <a href="https://www.zeitverschiebung.net/cn/city/551487"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kazan</a>, <a href="https://www.zeitverschiebung.net/cn/city/501175"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Rostov-na-Donu</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--simferopol">Europe/Simferopol</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/694423"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sevastopol</a>, <a href="https://www.zeitverschiebung.net/cn/city/693805"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Simferopol</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/706524"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kerch</a>, <a href="https://www.zeitverschiebung.net/cn/city/688105"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Yevpatoriya</a>, <a href="https://www.zeitverschiebung.net/cn/city/688533"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yalta</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--antananarivo">Indian/Antananarivo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mg"><span class="flag-icon flag-icon-mg ' \
       'mr-10"></span>Madagascar</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1070940"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Antananarivo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1053384"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Toamasina</a>, <a href="https://www.zeitverschiebung.net/cn/city/1069166"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Antsirabe</a>, <a href="https://www.zeitverschiebung.net/cn/city/1064890"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Fianarantsoa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1062663"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mahajanga</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--comoro">Indian/Comoro</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/km"><span class="flag-icon flag-icon-km ' \
       'mr-10"></span>Comoros</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/921772"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Moroni</a>, <a href="https://www.zeitverschiebung.net/cn/city/921753"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Moutsamoudou</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/921889"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Fomboni</a>, <a href="https://www.zeitverschiebung.net/cn/city/921906"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Domoni</a>, <a href="https://www.zeitverschiebung.net/cn/city/1091401"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Adda-Douéni</a> </td> </tr> <tr> <td><strong>UTC+3</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--mayotte">Indian/Mayotte</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/yt"><span class="flag-icon flag-icon-yt ' \
       'mr-10"></span>Mayotte</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/921815"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mamoudzou</a>, <a href="https://www.zeitverschiebung.net/cn/city/1090225"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Koungou</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/921900"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Dzaoudzi</a>, <a href="https://www.zeitverschiebung.net/cn/city/921917"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Dembeni</a>, <a href="https://www.zeitverschiebung.net/cn/city/1090340"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sada</a> </td> </tr> <tr> <td><strong>UTC+3:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--tehran">Asia/Tehran</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ir"><span class="flag-icon flag-icon-ir ' \
       'mr-10"></span>Iran</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/112931"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tehran</a>, <a href="https://www.zeitverschiebung.net/cn/city/124665"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mashhad</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/418863"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Isfahan</a>, <a href="https://www.zeitverschiebung.net/cn/city/128747"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Karaj</a>, <a href="https://www.zeitverschiebung.net/cn/city/113646"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tabriz</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--baku">Asia/Baku</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/az"><span class="flag-icon flag-icon-az ' \
       'mr-10"></span>Azerbaijan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/587084"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Baku</a>, <a href="https://www.zeitverschiebung.net/cn/city/586523"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ganja</a>, <a href="https://www.zeitverschiebung.net/cn/city/584923"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sumqayıt</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/147622"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Lankaran</a>, <a href="https://www.zeitverschiebung.net/cn/city/585514"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mingelchaur</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--dubai">Asia/Dubai</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ae"><span class="flag-icon flag-icon-ae ' \
       'mr-10"></span>United Arab Emirates</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/292223"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dubai</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/292968"><i class="fa fa-map-marker pr-5 pl-5"></i>Abu ' \
       'Dhabi</a>, <a href="https://www.zeitverschiebung.net/cn/city/292672"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sharjah</a>, <a href="https://www.zeitverschiebung.net/cn/city/292913"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Al Ain</a>, <a href="https://www.zeitverschiebung.net/cn/city/292932"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ajman</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--muscat">Asia/Muscat</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/om"><span class="flag-icon flag-icon-om ' \
       'mr-10"></span>Oman</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/287286"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Muscat</a>, <a href="https://www.zeitverschiebung.net/cn/city/288967"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Seeb</a>, <a href="https://www.zeitverschiebung.net/cn/city/286621"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Şalālah</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/288764"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bawshar</a>, <a href="https://www.zeitverschiebung.net/cn/city/286282"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sohar</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--tbilisi">Asia/Tbilisi</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ge"><span class="flag-icon flag-icon-ge ' \
       'mr-10"></span>Georgia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/611717"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tbilisi</a>, <a href="https://www.zeitverschiebung.net/cn/city/613607"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kutaisi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/615532"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Batumi</a>, <a href="https://www.zeitverschiebung.net/cn/city/611847"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sokhumi</a>, <a href="https://www.zeitverschiebung.net/cn/city/610824"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zugdidi</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--yerevan">Asia/Yerevan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/am"><span class="flag-icon flag-icon-am ' \
       'mr-10"></span>Armenia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/616052"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yerevan</a>, <a href="https://www.zeitverschiebung.net/cn/city/616635"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gyumri</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/616530"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Vanadzor</a>, <a href="https://www.zeitverschiebung.net/cn/city/616062"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ejmiatsin</a>, <a href="https://www.zeitverschiebung.net/cn/city/616629"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hrazdan</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--astrakhan">Europe/Astrakhan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/580497"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Astrakhan</a>, <a href="https://www.zeitverschiebung.net/cn/city/583798"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Akhtubinsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/831130"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Znamensk</a>, <a href="https://www.zeitverschiebung.net/cn/city/550671"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kharabali</a>, <a href="https://www.zeitverschiebung.net/cn/city/553248"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kamyzyak</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--samara">Europe/Samara</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/499099"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Samara</a>, <a href="https://www.zeitverschiebung.net/cn/city/482283"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tol’yatti</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/554840"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Izhevsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/484972"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Syzran’</a>, <a href="https://www.zeitverschiebung.net/cn/city/518659"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Novokuybyshevsk</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--saratov">Europe/Saratov</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--ulyanovsk">Europe/Ulyanovsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/europe--volgograd">Europe/Volgograd</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/472757"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Volgograd</a>, <a href="https://www.zeitverschiebung.net/cn/city/498677"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saratov</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/548408"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kirov</a>, <a href="https://www.zeitverschiebung.net/cn/city/472231"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Volzhskiy</a>, <a href="https://www.zeitverschiebung.net/cn/city/579492"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Balakovo</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--mahe">Indian/Mahe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sc"><span class="flag-icon flag-icon-sc ' \
       'mr-10"></span>Seychelles</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/241131"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Victoria</a>, <a href="https://www.zeitverschiebung.net/cn/city/241448"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Anse Boileau</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/241423"><i class="fa fa-map-marker pr-5 pl-5"></i>Bel ' \
       'Ombre</a>, <a href="https://www.zeitverschiebung.net/cn/city/241427"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Beau Vallon</a>, <a href="https://www.zeitverschiebung.net/cn/city/241395"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cascade</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--mauritius">Indian/Mauritius</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mu"><span class="flag-icon flag-icon-mu ' \
       'mr-10"></span>Mauritius</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/934154"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Port Louis</a>, <a href="https://www.zeitverschiebung.net/cn/city/933945"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Vacoas</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/934570"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Curepipe</a>, <a href="https://www.zeitverschiebung.net/cn/city/934131"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Quatre Bornes</a>, <a href="https://www.zeitverschiebung.net/cn/city/933959"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Triolet</a> </td> </tr> <tr> <td><strong>UTC+4</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--reunion">Indian/Reunion</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/re"><span class="flag-icon flag-icon-re ' \
       'mr-10"></span>Reunion</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/935264"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Saint-Denis</a>, <a href="https://www.zeitverschiebung.net/cn/city/935221"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saint-Paul</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/935214"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Saint-Pierre</a>, <a href="https://www.zeitverschiebung.net/cn/city/935582"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Le Tampon</a>, <a href="https://www.zeitverschiebung.net/cn/city/935268"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Saint-André</a> </td> </tr> <tr> <td><strong>UTC+4:30</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/asia--kabul">Asia/Kabul</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/af"><span class="flag-icon flag-icon-af ' \
       'mr-10"></span>Afghanistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1138958"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kabul</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1138336"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kandahār</a>, <a href="https://www.zeitverschiebung.net/cn/city/1133616"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Mazār-e Sharīf</a>, <a href="https://www.zeitverschiebung.net/cn/city/1140026"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Herāt</a>, <a href="https://www.zeitverschiebung.net/cn/city/1139715"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Jalālābād</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--mawson">Antarctica/Mawson</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--aqtau">Asia/Aqtau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/610612"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Aktau</a>, <a href="https://www.zeitverschiebung.net/cn/city/607610"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Zhanaozen</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/610298"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Beyneu</a>, <a href="https://www.zeitverschiebung.net/cn/city/608324"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Shetpe</a>, <a href="https://www.zeitverschiebung.net/cn/city/609919"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yeraliyev</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--aqtobe">Asia/Aqtobe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/610611"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Aqtöbe</a>, <a href="https://www.zeitverschiebung.net/cn/city/608679"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kandyagash</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/608359"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Shalqar</a>, <a href="https://www.zeitverschiebung.net/cn/city/609404"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Khromtau</a>, <a href="https://www.zeitverschiebung.net/cn/city/609924"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Embi</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--ashgabat">Asia/Ashgabat</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tm"><span class="flag-icon flag-icon-tm ' \
       'mr-10"></span>Turkmenistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/162183"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ashgabat</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1219649"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Türkmenabat</a>, <a href="https://www.zeitverschiebung.net/cn/city/601734"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Daşoguz</a>, <a href="https://www.zeitverschiebung.net/cn/city/1218667"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mary</a>, <a href="https://www.zeitverschiebung.net/cn/city/161616"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Balkanabat</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--atyrau">Asia/Atyrau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--dushanbe">Asia/Dushanbe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tj"><span class="flag-icon flag-icon-tj ' \
       'mr-10"></span>Tajikistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1221874"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dushanbe</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1514879"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Khŭjand</a>, <a href="https://www.zeitverschiebung.net/cn/city/1221194"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kŭlob</a>, <a href="https://www.zeitverschiebung.net/cn/city/1220747"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Qŭrghonteppa</a>, <a href="https://www.zeitverschiebung.net/cn/city/1220253"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Istaravshan</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/asia--karachi">Asia/Karachi</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pk"><span class="flag-icon flag-icon-pk ' \
       'mr-10"></span>Pakistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1174872"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Karachi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1172451"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lahore</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1179400"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Faisalābād</a>, <a href="https://www.zeitverschiebung.net/cn/city/1166993"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Rawalpindi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1169825"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Multān</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--oral">Asia/Oral</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/608668"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Oral</a>, <a href="https://www.zeitverschiebung.net/cn/city/610529"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Atyrau</a>, <a href="https://www.zeitverschiebung.net/cn/city/609123"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Qulsary</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/610613"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Aqsay</a>, <a href="https://www.zeitverschiebung.net/cn/city/608362"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Shalkar</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--qyzylorda">Asia/Qyzylorda</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1519922"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kyzylorda</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1519928"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kostanay</a>, <a href="https://www.zeitverschiebung.net/cn/city/1519843"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Rudnyy</a>, <a href="https://www.zeitverschiebung.net/cn/city/1516601"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dzhetygara</a>, <a href="https://www.zeitverschiebung.net/cn/city/1521315"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lisakovsk</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--samarkand">Asia/Samarkand</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/uz"><span class="flag-icon flag-icon-uz ' \
       'mr-10"></span>Uzbekistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1216265"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Samarqand</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1217662"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bukhara</a>, <a href="https://www.zeitverschiebung.net/cn/city/601294"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nukus</a>, <a href="https://www.zeitverschiebung.net/cn/city/1216311"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Qarshi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1513886"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Jizzax</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--tashkent">Asia/Tashkent</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/uz"><span class="flag-icon flag-icon-uz ' \
       'mr-10"></span>Uzbekistan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1512569"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tashkent</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1513157"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Namangan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1514588"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Andijon</a>, <a href="https://www.zeitverschiebung.net/cn/city/1512979"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Qo‘qon</a>, <a href="https://www.zeitverschiebung.net/cn/city/1514210"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chirchiq</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--yekaterinburg">Asia/Yekaterinburg</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1486209"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yekaterinburg</a>, <a href="https://www.zeitverschiebung.net/cn/city/1508291"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chelyabinsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/479561"><i class="fa fa-map-marker pr-5 pl-5"></i>Ufa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/511196"><i class="fa fa-map-marker pr-5 pl-5"></i>Perm</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/515003"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Orenburg</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--kerguelen">Indian/Kerguelen</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tf"><span class="flag-icon flag-icon-tf ' \
       'mr-10"></span>French Southern Territories</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/1546102"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Port-aux-Français</a> </td> </tr> <tr> <td><strong>UTC+5</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--maldives">Indian/Maldives</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mv"><span class="flag-icon flag-icon-mv ' \
       'mr-10"></span>Maldives</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1282027"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Male</a>, <a href="https://www.zeitverschiebung.net/cn/city/1337611"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Fuvahmulah</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1282256"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hithadhoo</a>, <a href="https://www.zeitverschiebung.net/cn/city/1337613"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kulhudhuffushi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1337610"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Thinadhoo</a> </td> </tr> <tr> <td><strong>UTC+5:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--colombo">Asia/Colombo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/lk"><span class="flag-icon flag-icon-lk mr-10"></span>Sri ' \
       'Lanka</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1248991"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Colombo</a>, <a href="https://www.zeitverschiebung.net/cn/city/1234569"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dehiwala-Mount Lavinia</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/9259456"><i class="fa fa-map-marker pr-5 pl-5"></i>Mount ' \
       'Lavinia</a>, <a href="https://www.zeitverschiebung.net/cn/city/1246321"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Galkissa</a>, <a href="https://www.zeitverschiebung.net/cn/city/1234633"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Moratuwa</a> </td> </tr> <tr> <td><strong>UTC+5:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--kolkata">Asia/Kolkata</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/in"><span class="flag-icon flag-icon-in ' \
       'mr-10"></span>India</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1275339"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mumbai</a>, <a href="https://www.zeitverschiebung.net/cn/city/1273294"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Delhi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1277333"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bengaluru</a>, <a href="https://www.zeitverschiebung.net/cn/city/1275004"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kolkata</a>, <a href="https://www.zeitverschiebung.net/cn/city/1264527"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Chennai</a> </td> </tr> <tr> <td><strong>UTC+5:45</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--kathmandu">Asia/Kathmandu</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/np"><span class="flag-icon flag-icon-np ' \
       'mr-10"></span>Nepal</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1283240"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kathmandu</a>, <a href="https://www.zeitverschiebung.net/cn/city/1282898"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pokhara</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1282931"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Pātan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1283582"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Biratnagar</a>, <a href="https://www.zeitverschiebung.net/cn/city/1283581"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bīrganj</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--vostok">Antarctica/Vostok</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--almaty">Asia/Almaty</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1526384"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Almaty</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/609655"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Karagandy</a>, <a href="https://www.zeitverschiebung.net/cn/city/1518980"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Shymkent</a>, <a href="https://www.zeitverschiebung.net/cn/city/1516905"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Taraz</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1526273"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Astana</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--bishkek">Asia/Bishkek</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kg"><span class="flag-icon flag-icon-kg ' \
       'mr-10"></span>Kyrgyzstan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1528675"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bishkek</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/11054823"><i class="fa fa-map-marker pr-5 pl-5"></i>Osh ' \
       'City</a>, <a href="https://www.zeitverschiebung.net/cn/city/1527534"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Osh</a>, <a href="https://www.zeitverschiebung.net/cn/city/1528249"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Jalal-Abad</a>, <a href="https://www.zeitverschiebung.net/cn/city/1528121"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Karakol</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--dhaka">Asia/Dhaka</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bd"><span class="flag-icon flag-icon-bd ' \
       'mr-10"></span>Bangladesh</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1185241"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dhaka</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1205733"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Chittagong</a>, <a href="https://www.zeitverschiebung.net/cn/city/1336135"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Khulna</a>, <a href="https://www.zeitverschiebung.net/cn/city/1185128"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rājshāhi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1185186"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Comilla</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--omsk">Asia/Omsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1496153"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Omsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1510018"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Biysk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1493467"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Rubtsovsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1497173"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Novoaltaysk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1506271"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gorno-Altaysk</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/asia--qostanay">Asia/Qostanay</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kz"><span class="flag-icon flag-icon-kz ' \
       'mr-10"></span>Kazakhstan</a></td> <td> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--thimphu">Asia/Thimphu</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bt"><span class="flag-icon flag-icon-bt ' \
       'mr-10"></span>Bhutan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1252416"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Thimphu</a>, <a href="https://www.zeitverschiebung.net/cn/city/1252479"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Punākha</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1252608"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tsirang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1252484"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Phuntsholing</a>, <a href="https://www.zeitverschiebung.net/cn/city/1337379"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pemagatshel</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--urumqi">Asia/Urumqi</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cn"><span class="flag-icon flag-icon-cn ' \
       'mr-10"></span>China</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1915223"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Zhongshan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1529102"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ürümqi</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1784990"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Zhanjiang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1529195"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Shihezi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1529114"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Turpan</a> </td> </tr> <tr> <td><strong>UTC+6</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--chagos">Indian/Chagos</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/io"><span class="flag-icon flag-icon-io ' \
       'mr-10"></span>British Indian Ocean Territory</a></td> <td> </td> </tr> <tr> ' \
       '<td><strong>UTC+6:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--yangon">Asia/Yangon</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mm"><span class="flag-icon flag-icon-mm ' \
       'mr-10"></span>Myanmar</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1298824"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yangon</a>, <a href="https://www.zeitverschiebung.net/cn/city/1311874"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mandalay</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6611854"><i class="fa fa-map-marker pr-5 pl-5"></i>Nay Pyi ' \
       'Taw</a>, <a href="https://www.zeitverschiebung.net/cn/city/1308465"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mawlamyine</a>, <a href="https://www.zeitverschiebung.net/cn/city/1300466"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bago</a> </td> </tr> <tr> <td><strong>UTC+6:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--cocos">Indian/Cocos</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cc"><span class="flag-icon flag-icon-cc mr-10"></span>Cocos ' \
       'Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/7304591"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>West Island</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--davis">Antarctica/Davis</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--bangkok">Asia/Bangkok</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/th"><span class="flag-icon flag-icon-th ' \
       'mr-10"></span>Thailand</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1609350"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bangkok</a>, <a href="https://www.zeitverschiebung.net/cn/city/1606590"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Samut Prakan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1608133"><i class="fa fa-map-marker pr-5 pl-5"></i>Mueang ' \
       'Nonthaburi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1605239"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Udon Thani</a>, <a href="https://www.zeitverschiebung.net/cn/city/1611110"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chon Buri</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--barnaul">Asia/Barnaul</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1510853"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Barnaul</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--hovd">Asia/Hovd</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mn"><span class="flag-icon flag-icon-mn ' \
       'mr-10"></span>Mongolia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1516048"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Khovd</a>, <a href="https://www.zeitverschiebung.net/cn/city/1515436"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ölgiy</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1515029"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ulaangom</a>, <a href="https://www.zeitverschiebung.net/cn/city/1515007"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Uliastay</a>, <a href="https://www.zeitverschiebung.net/cn/city/1516393"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Altai</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--ho_chi_minh">Asia/Ho_Chi_Minh</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/vn"><span class="flag-icon flag-icon-vn ' \
       'mr-10"></span>Vietnam</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1566083"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ho Chi Minh City</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1581130"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hanoi</a>, <a href="https://www.zeitverschiebung.net/cn/city/1583992"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Da Nang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1581298"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Haiphong</a>, <a href="https://www.zeitverschiebung.net/cn/city/1587923"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Biên Hòa</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--jakarta">Asia/Jakarta</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/id"><span class="flag-icon flag-icon-id ' \
       'mr-10"></span>Indonesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1642911"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Jakarta</a>, <a href="https://www.zeitverschiebung.net/cn/city/1625822"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Surabaya</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1214520"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Medan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1650357"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bandung</a>, <a href="https://www.zeitverschiebung.net/cn/city/1649378"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bekasi</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--krasnoyarsk">Asia/Krasnoyarsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1502026"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Krasnoyarsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1512236"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Abakan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1497337"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Norilsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1512165"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Achinsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1500973"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kyzyl</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--novokuznetsk">Asia/Novokuznetsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1496990"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Novokuznetsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1503901"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kemerovo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1494114"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Prokop’yevsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1500665"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Leninsk-Kuznetsky</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1503277"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kiselëvsk</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--novosibirsk">Asia/Novosibirsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1496747"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Novosibirsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1489425"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tomsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1538637"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Seversk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1510350"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Berdsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/1505429"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Iskitim</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--phnom_penh">Asia/Phnom_Penh</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kh"><span class="flag-icon flag-icon-kh ' \
       'mr-10"></span>Cambodia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1821306"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Phnom Penh</a>, <a href="https://www.zeitverschiebung.net/cn/city/1821940"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Takeo</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1831142"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sihanoukville</a>, <a href="https://www.zeitverschiebung.net/cn/city/1831797"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Battambang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1822214"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Siem Reap</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--pontianak">Asia/Pontianak</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/id"><span class="flag-icon flag-icon-id ' \
       'mr-10"></span>Indonesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1630789"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Pontianak</a>, <a href="https://www.zeitverschiebung.net/cn/city/1624863"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tanjungpinang</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1633118"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Palangkaraya</a>, <a href="https://www.zeitverschiebung.net/cn/city/1626916"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Singkawang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1628884"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Sampit</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--tomsk">Asia/Tomsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--vientiane">Asia/Vientiane</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/la"><span class="flag-icon flag-icon-la ' \
       'mr-10"></span>Laos</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1651944"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vientiane</a>, <a href="https://www.zeitverschiebung.net/cn/city/1654379"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Pakse</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1653316"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Savannakhét</a>, <a href="https://www.zeitverschiebung.net/cn/city/1655559"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Luang Prabang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1652203"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Xam Nua</a> </td> </tr> <tr> <td><strong>UTC+7</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/indian--christmas">Indian/Christmas</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cx"><span class="flag-icon flag-icon-cx ' \
       'mr-10"></span>Christmas Island</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2078127"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Flying Fish Cove</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/antarctica--casey">Antarctica/Casey</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--brunei">Asia/Brunei</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/bn"><span class="flag-icon flag-icon-bn ' \
       'mr-10"></span>Brunei</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1820906"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bandar Seri Begawan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1820491"><i class="fa fa-map-marker pr-5 pl-5"></i>Kuala ' \
       'Belait</a>, <a href="https://www.zeitverschiebung.net/cn/city/1820187"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Seria</a>, <a href="https://www.zeitverschiebung.net/cn/city/1820071"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tutong</a>, <a href="https://www.zeitverschiebung.net/cn/city/1820903"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Bangar</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--choibalsan">Asia/Choibalsan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mn"><span class="flag-icon flag-icon-mn ' \
       'mr-10"></span>Mongolia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2032614"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Baruun-Urt</a>, <a href="https://www.zeitverschiebung.net/cn/city/2032054"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Choibalsan</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--hong_kong">Asia/Hong_Kong</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/hk"><span class="flag-icon flag-icon-hk mr-10"></span>Hong ' \
       'Kong</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1819729"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hong Kong</a>, <a href="https://www.zeitverschiebung.net/cn/city/1819609"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kowloon</a>, <a href="https://www.zeitverschiebung.net/cn/city/1818209"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tsuen Wan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1818223"><i class="fa fa-map-marker pr-5 pl-5"></i>Yuen ' \
       'Long Kau Hui</a>, <a href="https://www.zeitverschiebung.net/cn/city/11101593"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tung Chung</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--irkutsk">Asia/Irkutsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2023469"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Irkutsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2014407"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ulan-Ude</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2051523"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bratsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2027667"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Angarsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2013952"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ust’-Ilimsk</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--kuala_lumpur">Asia/Kuala_Lumpur</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/my"><span class="flag-icon flag-icon-my ' \
       'mr-10"></span>Malaysia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1736376"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kota Bharu</a>, <a href="https://www.zeitverschiebung.net/cn/city/1735161"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kuala Lumpur</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1732905"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Klang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1771023"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kampung Baru Subang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1732752"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Johor Bahru</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/asia--kuching">Asia/Kuching</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/my"><span class="flag-icon flag-icon-my ' \
       'mr-10"></span>Malaysia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1735634"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kuching</a>, <a href="https://www.zeitverschiebung.net/cn/city/1733432"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kota Kinabalu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1734052"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sandakan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1734199"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tawau</a>, <a href="https://www.zeitverschiebung.net/cn/city/1738050"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Miri</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--macau">Asia/Macau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mo"><span class="flag-icon flag-icon-mo ' \
       'mr-10"></span>Macao</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1821274"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Macau</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--makassar">Asia/Makassar</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/id"><span class="flag-icon flag-icon-id ' \
       'mr-10"></span>Indonesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1622786"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Makassar</a>, <a href="https://www.zeitverschiebung.net/cn/city/1645528"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Denpasar</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/8224624"><i class="fa fa-map-marker pr-5 pl-5"></i>City of ' \
       'Balikpapan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1650213"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Banjarmasin</a>, <a href="https://www.zeitverschiebung.net/cn/city/1636544"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Manado</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--manila">Asia/Manila</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ph"><span class="flag-icon flag-icon-ph ' \
       'mr-10"></span>Philippines</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1692192"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Quezon City</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1701668"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Manila</a>, <a href="https://www.zeitverschiebung.net/cn/city/1723510"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Budta</a>, <a href="https://www.zeitverschiebung.net/cn/city/1715348"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Davao</a>, <a href="https://www.zeitverschiebung.net/cn/city/1978681"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Malingao</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--shanghai">Asia/Shanghai</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/cn"><span class="flag-icon flag-icon-cn ' \
       'mr-10"></span>China</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1796236"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Shanghai</a>, <a href="https://www.zeitverschiebung.net/cn/city/1816670"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Beijing</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1792947"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tianjin</a>, <a href="https://www.zeitverschiebung.net/cn/city/1809858"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Guangzhou</a>, <a href="https://www.zeitverschiebung.net/cn/city/1795565"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Shenzhen</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--singapore">Asia/Singapore</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sg"><span class="flag-icon flag-icon-sg ' \
       'mr-10"></span>Singapore</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1880252"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Singapore</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--taipei">Asia/Taipei</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tw"><span class="flag-icon flag-icon-tw ' \
       'mr-10"></span>Taiwan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1668341"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Taipei</a>, <a href="https://www.zeitverschiebung.net/cn/city/1673820"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kaohsiung</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1668399"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Taichung</a>, <a href="https://www.zeitverschiebung.net/cn/city/1668355"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Tainan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1670029"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Banqiao</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--ulaanbaatar">Asia/Ulaanbaatar</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mn"><span class="flag-icon flag-icon-mn ' \
       'mr-10"></span>Mongolia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2028462"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ulan Bator</a>, <a href="https://www.zeitverschiebung.net/cn/city/2031405"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Erdenet</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2031964"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Darhan</a>, <a href="https://www.zeitverschiebung.net/cn/city/2030474"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Hovd</a>, <a href="https://www.zeitverschiebung.net/cn/city/2029945"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Murun-kuren</a> </td> </tr> <tr> <td><strong>UTC+8</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--perth">Australia/Perth</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2063523"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Perth</a>, <a href="https://www.zeitverschiebung.net/cn/city/2062338"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Rockingham</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2067119"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mandurah</a>, <a href="https://www.zeitverschiebung.net/cn/city/2075432"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Bunbury</a>, <a href="https://www.zeitverschiebung.net/cn/city/2077579"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Armadale</a> </td> </tr> <tr> <td><strong>UTC+8:45</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--eucla">Australia/Eucla</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--chita">Asia/Chita</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--dili">Asia/Dili</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tl"><span class="flag-icon flag-icon-tl mr-10"></span>East ' \
       'Timor</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1645457"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Dili</a>, <a href="https://www.zeitverschiebung.net/cn/city/1937031"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Same</a>, <a href="https://www.zeitverschiebung.net/cn/city/1636670"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maliana</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1626459"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Suai</a>, <a href="https://www.zeitverschiebung.net/cn/city/1637730"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Liquica</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--jayapura">Asia/Jayapura</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/id"><span class="flag-icon flag-icon-id ' \
       'mr-10"></span>Indonesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1651531"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ambon</a>, <a href="https://www.zeitverschiebung.net/cn/city/2082600"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Jayapura</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1626542"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sorong</a>, <a href="https://www.zeitverschiebung.net/cn/city/1624041"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ternate</a>, <a href="https://www.zeitverschiebung.net/cn/city/2082727"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Abepura</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--khandyga">Asia/Khandyga</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--pyongyang">Asia/Pyongyang</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kp"><span class="flag-icon flag-icon-kp mr-10"></span>North ' \
       'Korea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1871859"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Pyongyang</a>, <a href="https://www.zeitverschiebung.net/cn/city/1877449"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hamhŭng</a>, <a href="https://www.zeitverschiebung.net/cn/city/1873757"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Namp’o</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1877030"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Hŭngnam</a>, <a href="https://www.zeitverschiebung.net/cn/city/1876373"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kaesŏng</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--seoul">Asia/Seoul</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/kr"><span class="flag-icon flag-icon-kr mr-10"></span>South ' \
       'Korea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1835848"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Seoul</a>, <a href="https://www.zeitverschiebung.net/cn/city/1838524"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Busan</a>, <a href="https://www.zeitverschiebung.net/cn/city/1843564"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Incheon</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1835329"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Daegu</a>, <a href="https://www.zeitverschiebung.net/cn/city/1835235"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Daejeon</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--tokyo">Asia/Tokyo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/jp"><span class="flag-icon flag-icon-jp ' \
       'mr-10"></span>Japan</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1850147"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tokyo</a>, <a href="https://www.zeitverschiebung.net/cn/city/1848354"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Yokohama</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/1853909"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Osaka</a>, <a href="https://www.zeitverschiebung.net/cn/city/1856057"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nagoya</a>, <a href="https://www.zeitverschiebung.net/cn/city/2128295"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sapporo</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--yakutsk">Asia/Yakutsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2025339"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Chita</a>, <a href="https://www.zeitverschiebung.net/cn/city/2013159"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Yakutsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2026609"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Blagoveshchensk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2026895"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Belogorsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2019309"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Neryungri</a> </td> </tr> <tr> <td><strong>UTC+9</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--palau">Pacific/Palau</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/pw"><span class="flag-icon flag-icon-pw ' \
       'mr-10"></span>Palau</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/1559446"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Koror</a>, <a href="https://www.zeitverschiebung.net/cn/city/7732415"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Koror Town</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7671223"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Kloulklubed</a>, <a href="https://www.zeitverschiebung.net/cn/city/1559543"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ulimang</a>, <a href="https://www.zeitverschiebung.net/cn/city/4038170"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mengellang</a> </td> </tr> <tr> <td><strong>UTC+9:30</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/australia--adelaide">Australia/Adelaide</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2078025"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Adelaide</a>, <a href="https://www.zeitverschiebung.net/cn/city/7302628"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Adelaide Hills</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2156643"><i class="fa fa-map-marker pr-5 pl-5"></i>Mount ' \
       'Gambier</a>, <a href="https://www.zeitverschiebung.net/cn/city/2065740"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Morphett Vale</a>, <a href="https://www.zeitverschiebung.net/cn/city/2062944"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Prospect</a> </td> </tr> <tr> <td><strong>UTC+9:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--broken_hill">Australia/Broken_Hill</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2173911"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Broken Hill</a> </td> </tr> <tr> <td><strong>UTC+9:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--darwin">Australia/Darwin</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2073124"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Darwin</a>, <a href="https://www.zeitverschiebung.net/cn/city/2077895"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Alice Springs</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/6301965"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Palmerston</a>, <a href="https://www.zeitverschiebung.net/cn/city/2068655"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Katherine</a>, <a href="https://www.zeitverschiebung.net/cn/city/2066653"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>McMinns Lagoon</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/timezone/antarctica--dumontdurville">Antarctica' \
       '/DumontDUrville</a></td> <td><a href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon ' \
       'flag-icon-aq mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--ust-nera">Asia/Ust-Nera</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--vladivostok">Asia/Vladivostok</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2013348"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Vladivostok</a>, <a href="https://www.zeitverschiebung.net/cn/city/2022890"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Khabarovsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2056752"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Khabarovsk Vtoroy</a>, <a href="https://www.zeitverschiebung.net/cn/city/2021851"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Komsomolsk-on-Amur</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2014006"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Ussuriysk</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--brisbane">Australia/Brisbane</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2174003"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Brisbane</a>, <a href="https://www.zeitverschiebung.net/cn/city/2165087"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Gold Coast</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7281838"><i class="fa fa-map-marker pr-5 pl-5"></i>Logan ' \
       'City</a>, <a href="https://www.zeitverschiebung.net/cn/city/2146142"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Townsville</a>, <a href="https://www.zeitverschiebung.net/cn/city/2172797"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Cairns</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--currie">Australia/Currie</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--hobart">Australia/Hobart</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2163355"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hobart</a>, <a href="https://www.zeitverschiebung.net/cn/city/2160517"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Launceston</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2173125"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Burnie</a>, <a href="https://www.zeitverschiebung.net/cn/city/2168943"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Devonport</a>, <a href="https://www.zeitverschiebung.net/cn/city/2161311"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Kingston</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--lindeman">Australia/Lindeman</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--melbourne">Australia/Melbourne</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2158177"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Melbourne</a>, <a href="https://www.zeitverschiebung.net/cn/city/2165798"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Geelong</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2176187"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bendigo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2177091"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ballarat</a>, <a href="https://www.zeitverschiebung.net/cn/city/2151716"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Reservoir</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--sydney">Australia/Sydney</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2147714"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Sydney</a>, <a href="https://www.zeitverschiebung.net/cn/city/2172517"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Canberra</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2155472"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Newcastle</a>, <a href="https://www.zeitverschiebung.net/cn/city/2171507"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Wollongong</a>, <a href="https://www.zeitverschiebung.net/cn/city/2159045"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Maitland</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--chuuk">Pacific/Chuuk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fm"><span class="flag-icon flag-icon-fm ' \
       'mr-10"></span>Micronesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2081114"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Weno Town</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7648112"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Colonia</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--guam">Pacific/Guam</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/gu"><span class="flag-icon flag-icon-gu ' \
       'mr-10"></span>Guam</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4043909"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Dededo Village</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4038794"><i class="fa fa-map-marker pr-5 pl-5"></i>Yigo ' \
       'Village</a>, <a href="https://www.zeitverschiebung.net/cn/city/4038659"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Tamuning-Tumon-Harmon Village</a>, <a href="https://www.zeitverschiebung.net/cn/city/7268049"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mangilao Village</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4043656"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Barrigada Village</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--port_moresby">Pacific/Port_Moresby</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/pg"><span class="flag-icon flag-icon-pg ' \
       'mr-10"></span>Papua New Guinea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2088122"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Port Moresby</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2092740"><i class="fa fa-map-marker pr-5 pl-5"></i>Lae</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2090409"><i class="fa fa-map-marker pr-5 pl-5"></i>Mount ' \
       'Hagen</a>, <a href="https://www.zeitverschiebung.net/cn/city/2088163"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Popondetta</a>, <a href="https://www.zeitverschiebung.net/cn/city/2091996"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Madang</a> </td> </tr> <tr> <td><strong>UTC+10</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--saipan">Pacific/Saipan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mp"><span class="flag-icon flag-icon-mp ' \
       'mr-10"></span>Northern Mariana Islands</a></td> <td> <a ' \
       'href="https://www.zeitverschiebung.net/cn/city/7828758"><i class="fa fa-map-marker pr-5 pl-5"></i>Saipan</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7267949"><i class="fa fa-map-marker pr-5 pl-5"></i>San Jose ' \
       'Village</a> </td> </tr> <tr> <td><strong>UTC+10:30</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/australia--lord_howe">Australia/Lord_Howe</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--macquarie">Antarctica/Macquarie</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/au"><span class="flag-icon flag-icon-au ' \
       'mr-10"></span>Australia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--magadan">Asia/Magadan</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2123628"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Magadan</a>, <a href="https://www.zeitverschiebung.net/cn/city/2120048"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ust-Nera</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2120864"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Susuman</a>, <a href="https://www.zeitverschiebung.net/cn/city/2122574"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Ola</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--sakhalin">Asia/Sakhalin</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2119441"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yuzhno-Sakhalinsk</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2124286"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Korsakov</a>, <a href="https://www.zeitverschiebung.net/cn/city/2124615"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Kholmsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2122614"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Okha</a>, <a href="https://www.zeitverschiebung.net/cn/city/2122894"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Nevel’sk</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--srednekolymsk">Asia/Srednekolymsk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--bougainville">Pacific/Bougainville</a></td> ' \
       '<td><a href="https://www.zeitverschiebung.net/cn/country/pg"><span class="flag-icon flag-icon-pg ' \
       'mr-10"></span>Papua New Guinea</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2100633"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Arawa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/8714539"><i class="fa fa-map-marker pr-5 pl-5"></i>Buka</a> ' \
       '</td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--efate">Pacific/Efate</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/vu"><span class="flag-icon flag-icon-vu ' \
       'mr-10"></span>Vanuatu</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2135171"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Port-Vila</a>, <a href="https://www.zeitverschiebung.net/cn/city/2136150"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Luganville</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2136825"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Isangel</a>, <a href="https://www.zeitverschiebung.net/cn/city/2134814"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Sola</a>, <a href="https://www.zeitverschiebung.net/cn/city/2136697"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Lakatoro</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--guadalcanal">Pacific/Guadalcanal</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/sb"><span class="flag-icon flag-icon-sb ' \
       'mr-10"></span>Solomon Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2108502"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Honiara</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2109701"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Auki</a>, <a href="https://www.zeitverschiebung.net/cn/city/2108857"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Gizo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2109528"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Buala</a>, <a href="https://www.zeitverschiebung.net/cn/city/2102384"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tulaghi</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--kosrae">Pacific/Kosrae</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fm"><span class="flag-icon flag-icon-fm ' \
       'mr-10"></span>Micronesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2081342"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Tofol</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--norfolk">Pacific/Norfolk</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nf"><span class="flag-icon flag-icon-nf ' \
       'mr-10"></span>Norfolk Island</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2161314"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kingston</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--noumea">Pacific/Noumea</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nc"><span class="flag-icon flag-icon-nc mr-10"></span>New ' \
       'Caledonia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2139521"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Nouméa</a>, <a href="https://www.zeitverschiebung.net/cn/city/2140066"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Mont-Dore</a>, <a href="https://www.zeitverschiebung.net/cn/city/2141394"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Dumbéa</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2138981"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Païta</a>, <a href="https://www.zeitverschiebung.net/cn/city/2137690"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Wé</a> </td> </tr> <tr> <td><strong>UTC+11</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--pohnpei">Pacific/Pohnpei</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fm"><span class="flag-icon flag-icon-fm ' \
       'mr-10"></span>Micronesia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4043034"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Kolonia</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2082038"><i class="fa fa-map-marker pr-5 pl-5"></i>Kolonia ' \
       'Town</a>, <a href="https://www.zeitverschiebung.net/cn/city/2081986"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Palikir - National Government Center</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/antarctica--mcmurdo">Antarctica/McMurdo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/aq"><span class="flag-icon flag-icon-aq ' \
       'mr-10"></span>Antarctica</a></td> <td> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--anadyr">Asia/Anadyr</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2127202"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Anadyr</a>, <a href="https://www.zeitverschiebung.net/cn/city/2126682"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Bilibino</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/asia--kamchatka">Asia/Kamchatka</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ru"><span class="flag-icon flag-icon-ru ' \
       'mr-10"></span>Russia</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2122104"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Petropavlovsk-Kamchatsky</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2119538"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Yelizovo</a>, <a href="https://www.zeitverschiebung.net/cn/city/2118647"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Vilyuchinsk</a>, <a href="https://www.zeitverschiebung.net/cn/city/2124440"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Klyuchi</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--auckland">Pacific/Auckland</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nz"><span class="flag-icon flag-icon-nz mr-10"></span>New ' \
       'Zealand</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2193733"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Auckland</a>, <a href="https://www.zeitverschiebung.net/cn/city/2179537"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Wellington</a>, <a href="https://www.zeitverschiebung.net/cn/city/2192362"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Christchurch</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2187404"><i class="fa fa-map-marker pr-5 pl-5"></i>Manukau ' \
       'City</a>, <a href="https://www.zeitverschiebung.net/cn/city/7302484"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Waitakere</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--fiji">Pacific/Fiji</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/fj"><span class="flag-icon flag-icon-fj ' \
       'mr-10"></span>Fiji</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2198148"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Suva</a>, <a href="https://www.zeitverschiebung.net/cn/city/2204506"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lautoka</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2202064"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Nadi</a>, <a href="https://www.zeitverschiebung.net/cn/city/2204582"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Labasa</a>, <a href="https://www.zeitverschiebung.net/cn/city/8335413"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ba</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--funafuti">Pacific/Funafuti</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tv"><span class="flag-icon flag-icon-tv ' \
       'mr-10"></span>Tuvalu</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2110394"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Funafuti</a>, <a href="https://www.zeitverschiebung.net/cn/city/7602373"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Savave Village</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2110322"><i class="fa fa-map-marker pr-5 pl-5"></i>Tanrake ' \
       'Village</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110302"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Toga Village</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110415"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Asau Village</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--kwajalein">Pacific/Kwajalein</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mh"><span class="flag-icon flag-icon-mh ' \
       'mr-10"></span>Marshall Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/7304467"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Ebaye</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7306526"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Jabat</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--majuro">Pacific/Majuro</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/mh"><span class="flag-icon flag-icon-mh ' \
       'mr-10"></span>Marshall Islands</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2113779"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Majuro</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7306514"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Arno</a>, <a href="https://www.zeitverschiebung.net/cn/city/2080422"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Jabor</a>, <a href="https://www.zeitverschiebung.net/cn/city/7306528"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Wotje</a>, <a href="https://www.zeitverschiebung.net/cn/city/7306516"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mili</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--nauru">Pacific/Nauru</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nr"><span class="flag-icon flag-icon-nr ' \
       'mr-10"></span>Nauru</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/7626461"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Yaren</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110427"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Baiti</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/2110450"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Anabar</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110421"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Uaboe</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110433"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Ijuw</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--tarawa">Pacific/Tarawa</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ki"><span class="flag-icon flag-icon-ki ' \
       'mr-10"></span>Kiribati</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/2110257"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Tarawa</a>, <a href="https://www.zeitverschiebung.net/cn/city/2110248"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Betio Village</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/7601774"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Bikenibeu Village</a> </td> </tr> <tr> <td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--wake">Pacific/Wake</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/um"><span class="flag-icon flag-icon-um ' \
       'mr-10"></span>United States Minor Outlying Islands</a></td> <td> </td> </tr> <tr> ' \
       '<td><strong>UTC+12</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--wallis">Pacific/Wallis</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/wf"><span class="flag-icon flag-icon-wf ' \
       'mr-10"></span>Wallis and Futuna</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4034821"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Mata-Utu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4034778"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Sigavé</a>, <a href="https://www.zeitverschiebung.net/cn/city/4034885"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Alo</a> </td> </tr> <tr> <td><strong>UTC+12:45</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--chatham">Pacific/Chatham</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/nz"><span class="flag-icon flag-icon-nz mr-10"></span>New ' \
       'Zealand</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4032804"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>Waitangi</a> </td> </tr> <tr> <td><strong>UTC+13</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--apia">Pacific/Apia</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ws"><span class="flag-icon flag-icon-ws ' \
       'mr-10"></span>Samoa</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4035413"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Apia</a>, <a href="https://www.zeitverschiebung.net/cn/city/7106456"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Asau</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4035196"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Mulifanua</a>, <a href="https://www.zeitverschiebung.net/cn/city/4035260"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Leulumoega</a>, <a href="https://www.zeitverschiebung.net/cn/city/4035249"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Lufilufi</a> </td> </tr> <tr> <td><strong>UTC+13</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--enderbury">Pacific/Enderbury</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ki"><span class="flag-icon flag-icon-ki ' \
       'mr-10"></span>Kiribati</a></td> <td> </td> </tr> <tr> <td><strong>UTC+13</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--fakaofo">Pacific/Fakaofo</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/tk"><span class="flag-icon flag-icon-tk ' \
       'mr-10"></span>Tokelau</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/7522183"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Atafu Village</a>, <a href="https://www.zeitverschiebung.net/cn/city/7522181"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Nukunonu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4031110"><i class="fa fa-map-marker pr-5 pl-5"></i>Fale old ' \
       'settlement</a> </td> </tr> <tr> <td><strong>UTC+13</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--tongatapu">Pacific/Tongatapu</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/to"><span class="flag-icon flag-icon-to ' \
       'mr-10"></span>Tonga</a></td> <td> <a href="https://www.zeitverschiebung.net/cn/city/4032402"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Nuku‘alofa</a>, <a href="https://www.zeitverschiebung.net/cn/city/4032420"><i ' \
       'class="fa fa-map-marker pr-5 pl-5"></i>Neiafu</a>, ' \
       '<a href="https://www.zeitverschiebung.net/cn/city/4032369"><i class="fa fa-map-marker pr-5 ' \
       'pl-5"></i>Pangai</a>, <a href="https://www.zeitverschiebung.net/cn/city/4032384"><i class="fa fa-map-marker ' \
       'pr-5 pl-5"></i>‘Ohonua</a>, <a href="https://www.zeitverschiebung.net/cn/city/4032619"><i class="fa ' \
       'fa-map-marker pr-5 pl-5"></i>Hihifo</a> </td> </tr> <tr> <td><strong>UTC+14</strong></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/timezone/pacific--kiritimati">Pacific/Kiritimati</a></td> <td><a ' \
       'href="https://www.zeitverschiebung.net/cn/country/ki"><span class="flag-icon flag-icon-ki ' \
       'mr-10"></span>Kiribati</a></td> <td> </td> </tr> </tbody> '


soups = BeautifulSoup(html, 'html.parser')
num = 1
result = {}

for i in soups.findAll('tr'):
    if not i:
        continue
    i1 = i.findAll('td')
    print(i1[1].a.text)
    print(i1[0].strong.text)
    exit()
    zone_text = i1[0].strong.text
    print(getattr(i1[1], 'a').text)
    print(getattr(i1[2], 'a').text)
    print(getattr(i1[3], 'a').text)
    exit()
    result[zone_text] = ''
    exit()
