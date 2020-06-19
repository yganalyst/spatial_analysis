
"""ref : https://www.osgeo.kr/17"""
from fiona.crs import from_string
## 위경도 좌표(기본)
epsg4326 = from_string("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

*#*# TM좌표(미터)
# 국가공간정보포털(용도지역, 건물통합정보, 토지이용, 연속지적도 등)
epsg5174 = from_string("+proj=tmerc +lat_0=38 +lon_0=127.0028902777778 +k=1 +x_0=200000 +y_0=500000 +ellps=bessel +units=m +no_defs +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43")

# 도로명주소 데이터(전자지도, 배경지도)
epsg5179 = from_string("+proj=tmerc +lat_0=38 +lon_0=127.5 +k=0.9996 +x_0=1000000 +y_0=2000000 +ellps=GRS80 +units=m +no_defs")

# 카카오맵(다음지도)
epsg5181 = from_string("+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=500000 +ellps=GRS80 +units=m +no_defs")
epsg5181_qgis = from_string("+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=500000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs") # qgis 좌표, 보정좌표값 존재

# 산림청(산림입지토양도), 한국교원대학교(초중고 학교 위치 및 학군)
epsg5186 = from_string("+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=600000 +ellps=GRS80 +units=m +no_defs")
