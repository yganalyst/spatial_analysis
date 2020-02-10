## 1. QGIS  

http://www.qgistutorials.com/ko/docs/getting_started_with_pyqgis.html  
=> python with qgis => pyqgis tutorial  
https://blog.naver.com/sms91_/221033746201  
=> qgis에서 csv불러오기 및 좌표 찍기  
https://progworks.tistory.com/10  
=> 좌표계 변환 및 저장  
https://somlab.tistory.com/11  
=> 시각화  
https://gisutd.tistory.com/7  
=> 시각화(등간격, 등분위, natural break 등 개념 설명)  
https://gis.stackexchange.com/questions/112687/fixing-geometry-validity-errors-in-qgis  
=> 유효하지않은 도형(polygon 등)일때 버퍼를 아주 살짝만 줘서 보완할 수 있음  
http://www.qgistutorials.com/ko/docs/performing_spatial_joins.html  
=> spatial join in qgis  
https://gis.stackexchange.com/questions/214893/calculating-proportional-area-of-polygon-within-another-layers-polygon-using-qg  
=> 두 폴리곤 레이어가 있고, 면적 대비 겹치는 부분의 포함 정도를 계산하고 싶을때  
https://www.biz-gis.com/index.php?mid=QnA&document_srl=218341  
=> 폴리곤 면적 계산 (길이 등도 계산가능, 지오메트리 도구)  
https://gis.stackexchange.com/questions/123444/creating-fishnet-grid-shapefile-in-qgis  
=> 폴리곤에 대한 격자 grid 생성 방법  
https://gis.stackexchange.com/questions/138281/making-centroids-for-vector-grid-in-qgis  
=> 격자grid 생성 후 centroid 추출  
https://gis.stackexchange.com/questions/27739/filling-column-with-consecutive-numbers-in-qgis  
=> field calculator에 row 번호 컬럼 추가하는 법( id만들떄)  
https://www.northrivergeographic.com/qgis-adding-x-y-coordinate  
=> point 데이터의 좌표 필드 추가하는 방법  
http://jonathansoma.com/lede/foundations-2018/qgis/points-in-polygon/  
=> 폴리곤 내부에 있는 포인트 개수 새기  
https://www.osgeo.kr/17  
=> 좌표계 설명 자료  
https://progworks.tistory.com/75   
=> dem raster image 데이터 시각화  
http://www.qgistutorials.com/ko/docs/3/origin_destination_matrix.html  
=> QGIS 네트워크 분석  
http://blog.daum.net/geoscience/1442    
=> QGIS service-area(iso-area)  

---

## 2. Python  

### geopandas  

https://datascienceschool.net/view-notebook/ef921dc25e01437b9b5c532ba3b89b02/  
-> geopandas 설명자료  
http://geopandas.org/   
-> geopandas 공식 설명자료  
https://stackoverflow.com/questions/38961816/geopandas-set-crs-on-points  
-> geoDataframe의 crs 관련 질문 (스택오버플로우)  
https://gis.stackexchange.com/questions/269243/create-a-polygon-grid-using-with-geopandas  
=> python에서 shp파일 읽어서 polygon에 대한 격자 grid 생성하기  
https://stackoverflow.com/questions/40818679/geopandas-difference-methode-between-polygon-and-points  
=> geopandas로 한 점에 대한 buffer 생성  
https://gis.stackexchange.com/questions/253224/geopandas-buffer-using-geodataframe-while-maintaining-the-dataframe  
=> geopandas buffer 쉬운 예제  
http://geopandas.org/mapping.html  
=> geopandas 공식 사이트  
https://gis.stackexchange.com/questions/301251/geopandas-import-csv-make-polygons-from-x-y-coordinates-based-on-id  
=> 그냥 pandas로 csv 읽어서 mapping을 이용해 geodataframe 생성하기  
https://gis.stackexchange.com/questions/80881/what-is-unit-of-shapely-length-attribute  
=> 두 Point간의 직선거리 계산 (shapely)  
https://stackoverflow.com/questions/11015252/countig-points-in-boxes-of-a-grid  
=> 2차원 그래프에서 grid를 만들고 해당 grid에 포함된 것 카운팅  
https://gis.stackexchange.com/questions/319546/converting-list-of-polygons-to-multipolygon-using-shapely  
=> 여러개의 폴리곤을 멀티폴리곤으로 만들기  
https://gis.stackexchange.com/questions/322589/rasterizing-polygon-grid-in-python-geopandas-rasterio?noredirect=1&lq=1  
=> python에서 grid 폴리곤 만들기  
https://stackoverflow.com/questions/38961816/geopandas-set-crs-on-points  
=> geopandas 좌표 정의 및 프로젝션  
https://gis.stackexchange.com/questions/306674/geopandas-spatial-join-and-count  
http://geopandas.org/reference/geopandas.sjoin.html  
=> geopandas spatial join  
https://www.biz-gis.com/index.php?mid=QnA&document_srl=224858   
=> 좌표계 5174 -> 5179 안맞는 오류  
https://gis.stackexchange.com/questions/299379/superposing-two-plots-with-geopandas-with-non-fill-colours-in-one-of-them  
=> Geodataframe 여러개의 레이어 겹쳐 그리기  
https://gis.stackexchange.com/questions/342512/intersection-tolerance-error-with-shapely   
=> Polygon의 각 변(edge)를 linestring으로 뽑아내기  
https://stackoverflow.com/questions/24415806/coordinates-of-the-closest-points-of-two-geometries-in-shapely   
=> 가장 가까운 거리에 해당하는 좌표점 구하기  
https://stackoverflow.com/questions/39338550/cut-a-polygon-with-two-lines-in-shapely  
=> line으로 polygon 짜르기!!!!!!!!!!  
https://gis.stackexchange.com/questions/277334/shapely-polygon-union-results-in-strange-artifacts-of-tiny-non-overlapping-area?rq=1  
=> shapely로 polygon 결합 (dissolve 하는 방법)  
http://geopandas.org/set_operations.html  
=> intersection, union, difference 등 폴리곤 shape 처리 도구 설명  
https://shapely.readthedocs.io/en/latest/manual.html#object.project  
=> interpolate <=> project 함수 설명  
https://stackoverflow.com/questions/13062334/polygon-intersection-error-in-shapely-shapely-geos-topologicalerror-the-opera  
=> 유효하지 않은 Polygon과 유효한 폴리곤  
https://stackoverflow.com/questions/31391209/valueerror-no-shapely-geometry-can-be-created-from-null-value  
=> polygon 두개 union 할때, topology 에러 보완 (buffer를 이용한 보정)  
https://m.blog.naver.com/PostView.nhn?blogId=yshmisopia&logNo=60152050508&proxyReferer=https%3A%2F%2Fwww.google.com%2F  
=> Rtree 구조  
https://www.crocus.co.kr/1288  
=> convex hull 알고리즘  
https://m.blog.naver.com/PostView.nhn?blogId=bloodsoda&logNo=221029163536&proxyReferer=https%3A%2F%2Fwww.google.com%2F  
=> convex hull 알고리즘 조금 쉬운 설명  
https://stackoverflow.com/questions/28260962/calculating-angles-between-line-segments-python-with-math-atan2  
=> 두 line 사이의 각도 구하기(math 라이브러리를 이용한, atan, 기울기 활용)  
https://m.blog.naver.com/PostView.nhn?blogId=tobsysco&logNo=90189688655&proxyReferer=https%3A%2F%2Fwww.google.com%2F  
=> 각도 구하기(tan 수학 이론 설명)  
https://assortrock.com/7  
=> tan 삼각함수공식 (알아야 이해가능)  
https://www.youtube.com/watch?v=Vs263mWhXFg  
=> raster 파일 merge, QGIS 툴 사용할 수도 있고, command에서 할수도 있고(2가지 방법)  


### 기타  
https://pythonhosted.org/planar/polygon.html  
=> 도형 접선 그릴때 유용한(tangent) planar 라이브러리  
