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

      <l-geo-json :geojson="getFederalLocations" :options="options"></l-geo-json>
    </l-map>
  </div>
</template>

<script>
// @ is an alias to /src
// import L from 'leaflet';

// import HelloWorld from '@/components/HelloWorld.vue'

import {Icon} from 'leaflet';
import {LMap, LMarker, LTileLayer, LGeoJson} from 'vue2-leaflet';
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
    LMarker,
    LGeoJson,
  },
  data() {
    return {
      url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
      zoom: 5,
      center: [55.77741961547338, 37.61614862414406],
      fillColor: "#e4ce7f",
    }
  },
  methods: {
    ...mapActions(['fetchLocations', 'fetchFederalSubjectsLocations']),
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
    },
    getColor(value) {
      return value > 20  ? '#636363' :
          value > 10   ? '#969696' :
              value > 5   ? '#BDBDBD' :
                  value > 3   ? '#D9D9D9' :
                                  '#F0F0F0';
    }
    },
  created() {
    this.fetchLocations();
    this.fetchFederalSubjectsLocations();
  },
  computed: {
    ...mapGetters(['getLocations', 'getFederalLocations']),
    options() {
      return {
        onEachFeature: this.onEachFeatureFunction
      };
    },
    onEachFeatureFunction() {
      return (feature, layer) => {
        const objCount = feature.properties.obj_count;
        layer.setStyle({
          fillColor: this.getColor(objCount),
          weight: 1,
          opacity: 1,
          color: 'black',
          fillOpacity: 0.7
        })
      }
    },


    }
}
</script>
<style>

.marker-cluster-small {
  background-color: #006d2c !important;
  color: white !important;
}
.marker-cluster-small div {
  background-color: #2ca25f !important;
  color: white !important;
}
.marker-cluster-medium {
  background-color: #b39800 !important;
  color: white !important;
}
.marker-cluster-medium div {
  background-color: #FFD700 !important;
  color: black !important;
}
.marker-cluster-large {
  background-color: #bd0026 !important;
  color: white !important;
}
.marker-cluster-large div {
  background-color: #e31a1c !important;
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