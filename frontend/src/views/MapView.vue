<template>
  <div >

    <l-map  style="height: calc(100vh - 56px)" :zoom="zoom" :center="center" :options="{attributionControl: false}">
      <l-control class="mapControl">
        <b-card sub-title="Управление картой">

            <b-form-checkbox
                class="fedCheckbox"
                id="checkbox-1"
                v-model="fedChecked">
              <p>Слой отображения субъектов РФ</p>
            </b-form-checkbox>

            <multiselect
                v-model="fedSelected"
                :options="getFederalsInfo"
                track-by="fedName"
                label="fedName"
                :close-on-select="false"
                :multiple="true"
                placeholder="Выберите субъект"
                selectLabel="Нажмите, чтобы выбрать"
                deselectLabel="Нажмите, чтобы убрать"
                selectedLabel="Выбрано">
            </multiselect>


        </b-card>
      </l-control>

      <l-control
          v-show="fedChecked"
          position="bottomright">
        <b-card sub-title="Легенда карты">
          <div>
            <div style="display: inline-block; background-color: #636363; width: 15px; height: 15px;"></div>
            <p style="display: inline-block; margin-left: 10px;">> 20</p>
          </div>
          <div>
            <div style="display: inline-block; background-color: #969696; width: 15px; height: 15px;"></div>
            <p style="display: inline-block; margin-left: 10px;">11-20</p>
          </div>
          <div>
            <div style="display: inline-block; background-color: #BDBDBD; width: 15px; height: 15px;"></div>
            <p style="display: inline-block; margin-left: 10px;">6-10</p>
          </div>
          <div>
            <div style="display: inline-block; background-color: #D9D9D9; width: 15px; height: 15px;"></div>
            <p style="display: inline-block; margin-left: 10px;">4-5</p>
          </div>
          <div>
            <div style="display: inline-block; background-color: #F0F0F0; width: 15px; height: 15px;"></div>
            <p style="display: inline-block; margin-left: 10px;">1-3</p>
          </div>
        </b-card>
      </l-control>

      <l-tile-layer :url="url" ></l-tile-layer>

      <l-marker-cluster>
        <l-marker @click="showModal" id="markerId" v-for="point in markers" :key="point.objId" :lat-lng="[point.latitude, point.longitude]">

        </l-marker>
        <b-modal ref="my-modal" hide-footer title="Using Component Methods">
          <div class="d-block text-center">
            <h3>Hello From My Modal!</h3>
          </div>
          <b-button class="mt-3" variant="outline-danger" block @click="hideModal">Close Me</b-button>
          <b-button class="mt-2" variant="outline-warning" block @click="toggleModal">Toggle Me</b-button>
        </b-modal>
      </l-marker-cluster>

      <l-geo-json :visible="fedChecked" :geojson="fedLayers" :options="layerOptions"></l-geo-json>
    </l-map>
  </div>
</template>

<script>
// @ is an alias to /src
import L from 'leaflet';

import {Icon} from 'leaflet';
import {LMap, LMarker, LTileLayer, LGeoJson, LControl} from 'vue2-leaflet';
import {mapActions, mapGetters} from "vuex";
import Multiselect from "vue-multiselect";


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
    LControl,
    Multiselect
  },
  data() {
    return {
      url: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
      zoom: 5,
      center: [55.77741961547338, 37.61614862414406],
      fillColor: "#e4ce7f",
      markers: [],
      fedLayers: [],
      fedChecked: false,
      fedSelected: []
    }
  },
  methods: {
    ...mapActions(['fetchLocations', 'fetchFederalSubjectsLocations', 'fetchFederalsInfo']),
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
      return value > 20 ? '#636363' :
          value > 10 ? '#969696' :
              value > 5 ? '#BDBDBD' :
                  value > 3 ? '#D9D9D9' :
                      '#F0F0F0';
    }
  },
  created() {
    this.fetchLocations();
    this.fetchFederalSubjectsLocations();
    this.fetchFederalsInfo()
  },
  computed: {
    ...mapGetters(['getLocations', 'getFederalLocations', 'getFederalsInfo']),
    layerOptions() {
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
    }
  },
  mounted() {
    this.$nextTick(() => {
      const controlEl = this.$el.querySelector('.mapControl');
      L.DomEvent.disableScrollPropagation(controlEl);
    });
  },
  watch: {
    fedSelected(val) {
      if (val.length !== 0) {
        const keys = val.map(obj => obj.fedId);
        this.fedLayers = this.getFederalLocations.filter(obj => keys.includes(obj.id))
        this.markers = this.getLocations.filter(obj => keys.includes(obj.fedId))
      } else {
        this.fedLayers = this.getFederalLocations
        this.markers = this.getLocations
      }
    },
    getFederalLocations(val) {
      this.fedLayers = val;
    },
    getLocations(val) {
      this.markers = val;
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>

/*.marker-cluster-small {*/
/*  background-color: #006d2c !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-small div {*/
/*  background-color: #2ca25f !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-medium {*/
/*  background-color: #b39800 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-medium div {*/
/*  background-color: #FFD700 !important;*/
/*  color: black !important;*/
/*}*/
/*.marker-cluster-large {*/
/*  background-color: #bd0026 !important;*/
/*  color: white !important;*/
/*}*/
/*.marker-cluster-large div {*/
/*  background-color: #e31a1c !important;*/
/*  color: white !important;*/
/*}*/


.marker-cluster-small {
  background-color: #807bb7 !important;
  color: white !important;
}
.marker-cluster-small div {
  background-color: #9e9ac8 !important;
  color: white !important;
}
.marker-cluster-medium {
  background-color: #6458a7 !important;
  color: white !important;
}
.marker-cluster-medium div {
  background-color: #756bb1 !important;
  color: white !important;
}
.marker-cluster-large {
  background-color: #472178 !important;
  color: white !important;
}
.marker-cluster-large div {
  background-color: #54278f !important;
  color: white !important;
}

.fedCheckbox .form-check-input {
  margin-right: 10px; /* Adjust the spacing as needed */
}

.mapControl {
  width: 500px;
}

.multiselect__tag {
  background: #3b1b64 !important;
}


</style>