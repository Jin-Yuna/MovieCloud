<template>
   <div id="map">
   </div>
</template>

<script>
let kakao = window.kakao

export default {
  name: "KakaoMap",
  data() {
    return {
      map: null,
      markerPositions: [
        [ this.$store.state.latitude, this.$store.state.longitude ],
      ],
      markers: [],
    }
  },
  // 지도 불러오기
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    }
    else {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src ='https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=fcf79d7950891e2a0bcbec183a0187dd'
      document.head.appendChild(script)
    }
  },
  methods: {
    // 지도 표시
    initMap() {
      const container = document.getElementById("map")
      const options = {
        center: new kakao.maps.LatLng(this.$store.state.latitude, this.$store.state.longitude),
        level: 5,
      }
      this.map = new kakao.maps.Map(container, options)
      this.displayMarker(this.markerPositions)
      },
    // 마커 표시
    displayMarker(markerPositions) {
    // 현재 표시되어 있는 marker들이 있으면 marker에 등록된 map 없애주기
    if (this.markers.length > 0) {
      this.markers.forEach((marker) => marker.setMap(null));
    }

    const positions = markerPositions.map(
      (position) => new kakao.maps.LatLng(...position)
    );
    
    // 마커 표시하기
    if (positions.length > 0) {
        this.markers = positions.map(
          (position) =>
            new kakao.maps.Marker({
              map: this.map,
              position,
            })
        );

        const bounds = positions.reduce(
          (bounds, latlng) => bounds.extend(latlng),
          new kakao.maps.LatLngBounds()
        );

        this.map.setBounds(bounds);
      }
    },
  }
}
</script>

<style>
#map {
  width: 100%;
  height: 600px;
}

</style>
