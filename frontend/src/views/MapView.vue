<template>
  <div class="mapContainer" >
    <l-map style="height: calc(100vh - 56px)" :zoom="zoom" :center="center" :options="{attributionControl: false}">
      <l-tile-layer :url="url" ></l-tile-layer>
      <l-marker-cluster>
        <l-marker @click="showModal" id="markerId" v-for="point in getLocations" :key="point.objId" :lat-lng="[point.latitude, point.longitude]">

        </l-marker>
        <b-modal ref="my-modal" hide-footer title="Using Component Methods">
          <div class="d-block text-center">
            <h3>Hello From My Modal!</h3>
          </div>
          <b-button class="mt-3" variant="outline-danger" block @click="hideModal">Close Me</b-button>
          <b-button class="mt-2" variant="outline-warning" block @click="toggleModal">Toggle Me</b-button>
        </b-modal>
      </l-marker-cluster>
<!--      <l-marker :lat-lng="markerLatLng"></l-marker>-->
    </l-map>
  </div>
</template>

<script>
// @ is an alias to /src
// import L from 'leaflet';

// import HelloWorld from '@/components/HelloWorld.vue'

import {Icon} from 'leaflet';
import {LMap, LMarker, LTileLayer} from 'vue2-leaflet';
import {mapActions, mapGetters} from "vuex";


delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

export default {
  name: 'HomeView',
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data() {
    return {
      url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
      zoom: 5,
      center: [55.77741961547338, 37.61614862414406],
    }
  },
  methods: {
    ...mapActions(['fetchLocations']),
    showModal() {
      this.$refs['my-modal'].show()
    },
    hideModal() {
      this.$refs['my-modal'].hide()
    },
    toggleModal() {
      // We pass the ID of the button that we want to return focus to
      // when the modal has hidden
      this.$refs['my-modal'].toggle('#toggle-btn')
    }
  },
  created() {
    this.fetchLocations();
  },
  computed: {
    ...mapGetters(['getLocations']),
    getMarkers() {
      let locations = this.getLocations;
      return locations.map(function (element) {
        return { 'coordinates': [element.latitude, element.longitude], 'id': element.objId};
      });
    }
  }
}
</script>
<style>
.marker-cluster-small {
  background-color: #b0add2 !important;
  color: white !important;
}
.marker-cluster-small div {
  background-color: #9e9ac8 !important;
  color: white !important;
}
.marker-cluster-medium {
  background-color: #928ac1 !important;
  color: white !important;
}
.marker-cluster-medium div {
  background-color: #756bb1 !important;
  color: white !important;
}
.marker-cluster-large {
  background-color: #6a31b4 !important;
  color: white !important;
}
.marker-cluster-large div {
  background-color: #54278f !important;
  color: white !important;
}


/*.marker-cluster-small {*/
/*  background-color: #807bb7 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-small div {*/
/*  background-color: #9e9ac8 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-medium {*/
/*  background-color: #6458a7 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-medium div {*/
/*  background-color: #756bb1 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-large {*/
/*  background-color: #472178 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-large div {*/
/*  background-color: #54278f !important;*/
/*  color: white !important;*/
/*}*/

</style>