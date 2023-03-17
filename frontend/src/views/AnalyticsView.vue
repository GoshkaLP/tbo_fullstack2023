<template>
  <div>
    <div id="chart">
      <b-card title="Распределение средств по типам спортивных комплексов" class="chartCard">
        <apexchart type="bar" height="350" :options="getFundingChartOptions" :series="getFundingSeries"></apexchart>
      </b-card>

      <b-card title="Распределение выделенного бюджета по годам" class="chartCard">
        <apexchart type="line" height="350" :options="getConstructionChartOptions" :series="getConstructionSeries"></apexchart>
      </b-card>

    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import {mapActions, mapGetters} from "vuex";
export default {
  name: "AnalyticsView",
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {

    }
  },
  methods: {
    ...mapActions(['fetchFundingSportTypes', 'fetchConstructionSportTypes']),
  },
  computed: {
    ...mapGetters(['getFundingSportTypes', 'getConstructionSportTypes']),
    getFundingChartOptions() {
      return {
        chart: {
          type: 'bar',
          height: 500,
          stacked: true,
          toolbar: {
            show: true
          },
          zoom: {
            enabled: true
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }],
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
            dataLabels: {
              total: {
                enabled: true,
                style: {
                  fontSize: '13px',
                  fontWeight: 900
                }
              }
            }
          },
        },
        xaxis: {
          type: 'category',
          categories: this.getFundingSportTypes.categories,
        },
        legend: {
          position: 'right',
          offsetY: 40
        },
        fill: {
          opacity: 1
        },
        dataLabels: {
          enabled: false,
        },
      }
    },
    getConstructionChartOptions() {
      return {
        chart: {
          height: 500,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'straight'
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'],
            opacity: 0.5
          },
        },
        xaxis: {
          categories: this.getConstructionSportTypes.categories
        }
      }
    },
    getFundingSeries() {
      return this.getFundingSportTypes.series;
    },
    getConstructionSeries() {
      return this.getConstructionSportTypes.series;
    }
  },
  created() {
    this.fetchFundingSportTypes();
    this.fetchConstructionSportTypes()
  }

}
</script>

<style scoped>
.chartCard {
  margin: 50px;
}
</style>