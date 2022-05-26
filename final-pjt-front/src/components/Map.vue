<template>
  <div>
    <div id="map">
    </div>
    <!-- 검색 결과 표시 -->
    <div class="results" v-for="result in results.documents " :key="result.id" @click="displayMarker(Positions)">
      <h4>>{{ result.place_name }}</h4>
      <p>{{ result.address_name }}</p>
   </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "KakaoMap",
  data() {
    return {
      map: null,
      Positions: [
        [ this.$store.state.location.latitude, this.$store.state.location.longitude ],
      ],
      results: '',
      markers: [],
    }
  },
  // 지도 불러오기
  mounted() {
    if ( !window.kakao || !window.kakao.maps ) {
      const script = document.createElement("script")
      script.src ='https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=fcf79d7950891e2a0bcbec183a0187dd&libraries=services'
      script.onload = () => window.kakao.maps.load(this.initMap)
      document.head.appendChild(script)
    }
    else {
      this.initMap();
    }
  },
  methods: {
    // 지도 표시
    initMap() {
      const container = document.getElementById("map")
      const options = {
        center: new window.kakao.maps.LatLng(this.$store.state.location.latitude, this.$store.state.location.longitude),
        level: 8,
      }
      this.map = new window.kakao.maps.Map(container, options)
      this.searchPlaces()
      
      this.displayInfoWindow()
      this.displayMarker(this.Positions)   
      },
    // 마커 표시
    displayMarker(markerPositions) {
      // 현재 표시되어 있는 marker들이 있으면 marker에 등록된 map 없애주기
      if (this.markers.length > 0) {
        this.markers.forEach((marker) => marker.setMap(null))
      }
      const positions = markerPositions.map(
        (position) => new window.kakao.maps.LatLng(...position)
      );
    
      // 마커 표시하기
      if (positions.length > 0) {
        this.markers = positions.map((position) => new window.kakao.maps.Marker({
              map: this.map,
              position,
            }))

        const bounds = positions.reduce((bounds, latlng) => bounds.extend(latlng), new window.kakao.maps.LatLngBounds())
        this.map.setBounds(bounds)
      }
    },
    searchPlaces() {
      var config = { headers: { 'Authorization': 'KakaoAK 683d19aa3f66f6c7d4ca3b08f6f139ed'}};
      var url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query='+'영화관&'+`y=${this.$store.state.location.latitude}&`+`x=${this.$store.state.location.longitude}`+'&radius=20000'
        axios.get(url, config).then((response) => {
          // 데이터 개수 response.data.documents.length
          
          this.results = response.data

          for (var i=0; i< this.results.documents.length; i++){
            var latitude = Number(this.results.documents[i].y)
            var longitude = Number(this.results.documents[i].x)
            this.Positions.push([latitude, longitude])
          }
        }
			)
    },
    // 내 위치 표시
    displayInfoWindow() {
      if (this.infowindow && this.infowindow.getMap()) {
        //이미 생성한 인포윈도우가 있기 때문에 지도 중심좌표를 인포윈도우 좌표로 이동시킨다.
        this.map.setCenter(this.infowindow.getPosition());
        return;
      }

      var iwContent = '<div style="padding:5px;">내 위치</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
        iwPosition = new window.kakao.maps.LatLng(this.Positions[0][0], this.Positions[0][1]), //인포윈도우 표시 위치입니다
        iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

      this.infowindow = new window.kakao.maps.InfoWindow({
        map: this.map, // 인포윈도우가 표시될 지도
        position: iwPosition,
        content: iwContent,
        removable: iwRemoveable,
      });

      this.map.setCenter(iwPosition);
    },
    showPlace() {

    }
  },
}
</script>

<style>
#map {
  width: 900px;
  height: 600px;
}

</style>
