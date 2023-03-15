<template>
  <div >
    <l-map  style="height: calc(100vh - 56px)" :zoom="zoom" :center="center" :options="{attributionControl: false}">
      <l-control class="mapControl">
        <b-card sub-title="Управление картой">

            <b-form-checkbox
                id="checkbox-1"
                v-model="fedChecked">
              <p class="fedCheckbox">Слой отображения субъектов РФ</p>
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
          <p>Количество объектов</p>
          <MapLegendElement color="#636363">>20</MapLegendElement>
          <MapLegendElement color="#969696">11-20</MapLegendElement>
          <MapLegendElement color="#BDBDBD">6-10</MapLegendElement>
          <MapLegendElement color="#D9D9D9">4-5</MapLegendElement>
          <MapLegendElement color="#F0F0F0">1-3</MapLegendElement>
        </b-card>
      </l-control>

      <l-control class="markerInfo"
                 v-show="showLocationInfo"
                 position="topleft">

        <b-card sub-title="Здесь название комплекса)">
          <div class="text-center">
            <b-spinner v-if="!getLocationInfoStatus"></b-spinner>
          </div>
          <div class="scrollable-tab" v-if="getLocationInfoStatus">
            <b-tabs>
              <b-tab title="Общая информация" active>
                <b-card-body sub-title="Адрес">
                  <p>{{getLocationInfo.address}}</p>
                </b-card-body>
                <b-card-body sub-title="Описание">
                  <p>{{getLocationInfo.description}}</p>
                </b-card-body>
                <b-card-body sub-title="МО">
                  <p>{{getLocationInfo.municipalityEntity}}</p>
                </b-card-body>
                <b-card-body sub-title="Тип спортивного комплекса">
                  <p>{{getLocationInfo.sportsComplexType}}</p>
                </b-card-body>
                <b-card-body sub-title="Типы спорта">
                  <p>{{getLocationInfo.sportsTypes}}</p>
                </b-card-body>
                <b-card-body sub-title="Вебсайт">
                  <p>{{getLocationInfo.websiteUrl}}</p>
                </b-card-body>
                <b-card-body sub-title="Время работы">
                  <p>{{getLocationInfo.workHoursWeekdays}}</p>
                  <p>{{getLocationInfo.saturdayWorkingHours}}</p>
                  <p>{{getLocationInfo.sundayWorkingHours}}</p>
                </b-card-body>
              </b-tab>
              <b-tab title="Траты">
                <!-- Content for Tab 2 -->
              </b-tab>
              <b-tab title="Управляющий">
                <!-- Content for Tab 3 -->
              </b-tab>
            </b-tabs>
          </div>

<!--          <p v-if="getLocationInfoStatus" class="my-4">{{getLocationInfo}}</p>-->
        </b-card>
      </l-control>

      <l-tile-layer :url="url" ></l-tile-layer>

      <l-marker-cluster>
        <l-marker @click="showMarker(point.objId)" v-for="point in markers" :key="point.objId" :lat-lng="[point.latitude, point.longitude]">
        </l-marker>

<!--        <b-modal ref="my-modal" title="BootstrapVue">-->
<!--          <div class="text-center">-->
<!--            <b-spinner v-if="!getLocationInfoStatus"></b-spinner>-->
<!--          </div>-->
<!--          <p v-if="getLocationInfoStatus" class="my-4">{{getLocationInfo}}</p>-->
<!--        </b-modal>-->

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
import MapLegendElement from "@/components/MapLegendElement.vue";


delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});


export default {
  name: 'HomeView',
  components: {
    MapLegendElement,
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
      fedSelected: [],
      showLocationInfo: false
    }
  },
  methods: {
    ...mapActions(['fetchLocations', 'fetchFederalSubjectsLocations', 'fetchFederalsInfo', 'fetchLocationInfo']),
    showMarker(objId) {
      this.fetchLocationInfo(objId)
      this.showLocationInfo = !this.showLocationInfo;
      // this.$refs['my-modal'].show()
    },
    // hideModal() {
    //   this.$refs['my-modal'].hide()
    // },
    // toggleModal() {
    //   // We pass the ID of the button that we want to return focus to
    //   // when the modal has hidden
    //   this.$refs['my-modal'].toggle('#toggle-btn')
    // },
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
    ...mapGetters(['getLocations', 'getFederalLocations', 'getFederalsInfo', 'getLocationInfo', 'getLocationInfoStatus']),
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
      L.DomEvent.disableScrollPropagation(this.$el.querySelector('.markerInfo'));
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

.fedCheckbox {
  padding-left: 10px;
}

.mapControl {
  width: 500px;
}

.markerInfo {
  width: 400px;
}

.multiselect__tag {
  background: #3b1b64 !important;
}

.scrollable-tab {
  height: 500px; /* Set the desired height */
  overflow-y: scroll;
}


</style>