<template>
   <div id="map">
   </div>
</template>

<script>
export default {
  name: "KakaoMap",
  data() {
    return {
      map: null,
      markerPositions: [
        { title: '현재 위치', 
        latlng: new window.kakao.maps.LatLng(this.$store.state.latitude, this.$store.state.longitude) },
      ],
      markers: [],
    }
  },
  methods: {
    // 지도 표시
    initMap() {
      const container = document.getElementById("map")
      const options = {
        center: new window.kakao.maps.LatLng(this.$store.state.latitude, this.$store.state.longitude),
        level: 5,
      }
      this.map = new window.kakao.maps.Map(container, options)
      },
    // 마커 표시
    displayMarker(positions) {
    // 현재 표시되어 있는 marker들이 있으면 marker에 등록된 map 없애주기
    if (this.markers.length > 0) {
      this.markers.forEach((marker) => marker.setMap(null));
    }

    // 마커 이미지 커스터마이징
    const imgSrc = require('@/assets/marker.png')
    const imgSize = new window.kakao.maps.Size(24, 35)
    const markerImage = new window.kakao.maps.MarkerImage(imgSrc, imgSize)
    
    // 마커 표시하기
    positions.forEach((position) => {
      const marker = new window.kakao.maps.Marker({
        map: this.map,
        position: position.latlng,
        title: position.title,  // 마우스 오버시 표시할 제목
        image: markerImage,
      })
      this.markers.push(marker)
    })
      // 지도 이동
      const bounds = positions.reduce(
        (bounds, position) => bounds.extend(position.latlng),
        new window.kakao.maps.LatLngBounds()
      );

      this.map.setBounds(bounds);
    }
    },
    // 지도 불러오기
    mounted() {
      if (!window.kakao || !window.kakao.maps) {
        const script = document.createElement("script");
        script.src ='https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=fcf79d7950891e2a0bcbec183a0187dd'
        script.addEventListener("load", () => {
          window.kakao.maps.load(this.initMap)
        })
        document.head.appendChild(script)
      } else {
        this.initMap()
     }
  },
}
</script>

<style>
#map {
  width: 400px;
  height: 400px;
}

</style>