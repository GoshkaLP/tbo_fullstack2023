<template>
  <div>
    <l-map style="height: calc(100vh - 56px)" :zoom="mapZoom" :center="mapCenter" :options="{attributionControl: false}">
      <l-control class="mapControl">
        <b-card sub-title="Управление картой">
          <b-list-group flush>
            <b-list-group-item></b-list-group-item>
            <b-list-group-item>

                <b-form-checkbox
                    style="font-size: 16px"
                    id="fedCheckbox"
                    v-model="fedChecked">
                  Аналитика регионов
                </b-form-checkbox>
              <br>
              <p>Визуализация распределения спортивных объектов по субъектам РФ</p>
              <multiselect
                  :disabled="hexagonChecked"
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
            </b-list-group-item>

            <b-list-group-item>

              <b-form-checkbox
                  style="font-size: 16px"
                  id="hexagonCheckbox"
                  v-model="hexagonChecked">
                Временная линия
              </b-form-checkbox>
              <br>
              <p>Хронология появления новых спортивных объъектов в России</p>
              <b-form-group
                  label-cols="1"
                  label-align="left"
                  label="Год"
                  label-for="hexagonYear">
                <b-form-input id="hexagonYear" type="range" min="1997" max="2015" v-model="hexagonDateRange" :disabled="!hexagonChecked"></b-form-input>
              </b-form-group>
            </b-list-group-item>
          </b-list-group>

        </b-card>
      </l-control>

      <l-control
          v-show="fedChecked"
          position="bottomright">
        <b-card sub-title="Аналитика регионов">
          <p>Количество сопрт-объектов</p>
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

        <b-card :sub-title="getLocationInfo.info.name">
            <button type="button" class="close"
                    @click="hideMarker"
                    data-dismiss="modal" style="position: absolute; right: 10px;">×
            </button>

          <div class="text-center">
            <b-spinner v-if="!getLocationInfoStatus"></b-spinner>
          </div>
          <div class="scrollable-tab" v-if="getLocationInfoStatus">
            <b-tabs>
              <b-tab title="Общая информация" active>
                <b-card-body sub-title="Адрес">
                  <p>{{getLocationInfo.info.address}}</p>
                </b-card-body>
                <b-card-body sub-title="Описание">
                  <p>{{getLocationInfo.info.description}}</p>
                </b-card-body>
                <b-card-body sub-title="МО">
                  <p>{{getLocationInfo.info.municipalityEntity}}</p>
                </b-card-body>
                <b-card-body sub-title="Тип спортивного комплекса">
                  <p>{{getLocationInfo.info.sportsComplexType}}</p>
                </b-card-body>
                <b-card-body sub-title="Типы спорта">
                  <p>{{getLocationInfo.info.sportsTypes}}</p>
                </b-card-body>
              </b-tab>
              <b-tab title="Траты">
                <b-card-body sub-title="Действия с объектом">
                  <p>{{getLocationInfo.spending.objectActions}}</p>
                </b-card-body>
                <b-card-body sub-title="Даты проведения действий">
                  <p>{{getLocationInfo.spending.constructionStartDate}} - {{getLocationInfo.spending.constructionEndDate}}</p>
                </b-card-body>
                <b-card-body sub-title="Траты из разных источников">
                  <div id="chart">
                    <apexchart type="pie" :options="fundingChartOptions" :series="getFundingChartSeries"></apexchart>
                  </div>
                </b-card-body>

              </b-tab>
              <b-tab title="Контакты">
                <b-card-body sub-title="Курирующий орган">
                  <p>{{getLocationInfo.supervisory.supervisoryAuthority}}</p>
                </b-card-body>
                <b-card-body sub-title="Телефон курирующего органа">
                  <p>{{getLocationInfo.supervisory.supervisoryAuthorityPhone}}</p>
                </b-card-body>
                <b-card-body sub-title="Контакткный телефон объекта">
                  <p>{{getLocationInfo.supervisory.contactPhone}}</p>
                </b-card-body>
                <b-card-body sub-title="Электронная почта объекта">
                  <p>{{getLocationInfo.supervisory.email}}</p>
                </b-card-body>
                <b-card-body sub-title="Вебсайт">
                  <p>{{getLocationInfo.supervisory.websiteUrl}}</p>
                </b-card-body>
                <b-card-body sub-title="Время работы">
                  <p>{{getLocationInfo.supervisory.workHoursWeekdays}}</p>
                  <p>{{getLocationInfo.supervisory.saturdayWorkingHours}}</p>
                  <p>{{getLocationInfo.supervisory.sundayWorkingHours}}</p>
                </b-card-body>
              </b-tab>
            </b-tabs>
          </div>
        </b-card>
      </l-control>

      <l-control
      position="bottomleft">
        <b-card :sub-title="`Временная линия: ${hexagonDateRange} год`"
                v-show="hexagonChecked">
          <MapLegendElement color="#F9F0FB">футбольное поле</MapLegendElement>
          <MapLegendElement color="#F0E1F6">многофункциональный спортивный комплекс</MapLegendElement>
          <MapLegendElement color="#E6CCE3">стадион</MapLegendElement>
          <MapLegendElement color="#D9B3D9">арена ледовая</MapLegendElement>
          <MapLegendElement color="#C99DD3">канал гребной</MapLegendElement>
          <MapLegendElement color="#B58FCB">зал спортивный</MapLegendElement>
          <MapLegendElement color="#A17DB5">бассейн</MapLegendElement>
          <MapLegendElement color="#906CA9">площадка спортивная</MapLegendElement>
          <MapLegendElement color="#7E5D9B">комплекс биатлонно-лыжный</MapLegendElement>
          <MapLegendElement color="#6A4E8C">манеж легкоатлетический</MapLegendElement>
          <MapLegendElement color="#583D7A">трасса спортивная</MapLegendElement>
          <MapLegendElement color="#472C62">комплекс лыжный</MapLegendElement>
          <MapLegendElement color="#3F1E4F">комплекс горнолыжный</MapLegendElement>
        </b-card>
      </l-control>

      <l-tile-layer :url="mapUrl"></l-tile-layer>

      <l-marker-cluster>
        <l-marker
            :visible="!hexagonChecked"
            @click="showMarker(point.objId)" v-for="point in markers" :key="point.objId" :lat-lng="[point.latitude, point.longitude]">
        </l-marker>
      </l-marker-cluster>

      <l-geo-json :visible="fedChecked" :geojson="fedLayers" :options="federalLayerOptions"></l-geo-json>
      <l-geo-json :visible="hexagonChecked" :geojson="hexagonLayers" :options="hexagonLayerOptions"></l-geo-json>

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

import VueApexCharts from "vue-apexcharts";


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
    Multiselect,
    apexchart: VueApexCharts
  },
  data() {
    return {
      mapUrl: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
      mapZoom: 5,
      mapCenter: [55.77741961547338, 37.61614862414406],
      markers: [],
      fedLayers: [],
      fedChecked: false,
      fedSelected: [],
      showLocationInfo: false,
      hexagonLayers: [],
      hexagonDateRange: 1997,
      hexagonChecked: false,
      fundingChartOptions: {
        chart: {
          width: 200,
          type: 'pie',
        },
        labels: ['Фед. бюджет',
          'Субъект федерации',
          'МО',
          'Внебюджетные'],

      },
    }
  },
  methods: {
    ...mapActions(['fetchLocations', 'fetchFederalSubjectsLocations', 'fetchFederalsInfo', 'fetchLocationInfo', 'fetchHexagonLocations']),
    showMarker(objId) {
      this.fetchLocationInfo(objId)
      this.showLocationInfo = true;
    },
    hideMarker() {
      this.showLocationInfo = false;
    },
    getSubjectColor(value) {
      return value > 20 ? '#636363' :
          value > 10 ? '#969696' :
          value > 5 ? '#BDBDBD' :
          value > 3 ? '#D9D9D9' :
                      '#F0F0F0';
    },
    getHexagonColor(value) {
      return value === 'футбольное поле ' ? '#F9F0FB' :
            value === 'многофункциональный спортивный комплекс' ? '#F0E1F6' :
            value === 'стадион' ? '#E6CCE3' :
            value === 'арена ледовая' ? '#D9B3D9' :
            value === 'канал гребной' ? '#C99DD3' :
            value === 'зал спортивный' ? '#B58FCB' :
            value === 'бассейн' ? '#A17DB5' :
            value === 'площадка спортивная' ? '#906CA9' :
            value === 'комплекс биатлонно-лыжный' ? '#7E5D9B' :
            value === 'манеж легкоатлетический' ? '#6A4E8C' :
            value === 'трасса спортивная' ? '#583D7A' :
            value === 'комплекс лыжный' ? '#472C62' :
            '#3F1E4F';
    }
  },
  created() {
    this.fetchLocations();
    this.fetchFederalSubjectsLocations();
    this.fetchFederalsInfo()
    this.fetchHexagonLocations()
  },
  computed: {
    ...mapGetters(['getLocations', 'getFederalLocations', 'getFederalsInfo', 'getLocationInfo', 'getLocationInfoStatus',
    'getHexagonLocations']),
    federalLayerOptions() {
      return {
        onEachFeature: this.onEachFeatureFederal
      };
    },
    hexagonLayerOptions() {
      return {
        onEachFeature: this.onEachFeatureHexagon
      }
    },
    onEachFeatureFederal() {
      return (feature, layer) => {
        const objCount = feature.properties.obj_count;
        layer.setStyle({
          fillColor: this.getSubjectColor(objCount),
          weight: 1,
          opacity: 1,
          color: 'black',
          fillOpacity: 0.7
        })
      }
    },
    onEachFeatureHexagon() {
      return (feature, layer) => {
        const objSportType = feature.properties.sports_complex_type;
        layer.setStyle({
          fillColor: this.getHexagonColor(objSportType),
          weight: 2,
          opacity: 1,
          color: 'black',
          fillOpacity: 0.7
        })
      }
    },
    getFundingChartSeries() {
      return [this.getLocationInfo.spending.federalBudgetFunding,
        this.getLocationInfo.spending.regionalBudgetFunding, this.getLocationInfo.spending.localBudgetFunding,
        this.getLocationInfo.spending.offBudgetFunding];
    }
  },
  mounted() {
    this.$nextTick(() => {
      L.DomEvent.disableScrollPropagation(this.$el.querySelector('.mapControl'));
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
    },
    hexagonDateRange(val) {
      this.hexagonLayers = this.getHexagonLocations.filter(obj => obj.properties.construction_start_date <= val);
    },
    hexagonChecked(val) {
      if (val === false) {
        this.hexagonDateRange = 1997;
      }
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>

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

.controlText {
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

.card-subtitle {
  color: black !important;
}

</style>