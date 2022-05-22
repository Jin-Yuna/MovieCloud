<template>
  <div>
    <div id="map">
    </div>
    <!-- 검색 결과 표시 -->
    <div class="results" v-for="result in search.results" :key="result.id" @click="showPlace">
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
      markerPositions: [
        [ this.$store.state.latitude, this.$store.state.longitude ],
      ],
      markers: [],
      search: {
        pgn: null,
        results: [],
      }
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
        center: new window.kakao.maps.LatLng(this.$store.state.latitude, this.$store.state.longitude),
        level: 8,
      }
      this.map = new window.kakao.maps.Map(container, options)
      this.displayMarker(this.markerPositions)
      this.searchPlaces()
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
      var url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query='+'영화관&'+`y=${this.$store.state.latitude}&`+`x=${this.$store.state.longitude}`+'&radius=20000'
        axios.get(url, config).then(function(response) {
        console.log(JSON.stringify(response.data));
			})
    },
  },
}
</script>

<style>
#map {
  width: 100%;
  height: 600px;
}

</style>
