<template>
    <v-card>
      <v-container>
        <v-card-title>
          <span>Buscar</span>
        </v-card-title>
        <v-card-text>
          <v-form v-model="valid">
            <v-row>
              <v-col>
                <v-select
                v-model="selectedPropertiType"
                :items="propertiesType"
                label="Tipo Inmueble"
                ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="amountMin" label="Precio minimo"/>
              </v-col>
              <v-col>
                <v-text-field v-model="amountMax" label="Precio maximo"/>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-autocomplete v-model="selectedRoom" label="Ambientes" :items="rooms" />
                <!-- <v-subheader class="pl-0">
                Show thumb when using slider
              </v-subheader>
              <v-slider
              v-model="slider"
              thumb-label
              ></v-slider> -->
                </v-col>
              <v-col>
                <v-autocomplete v-model="selectedBedroom" label="Dormitorios" :items="bedRooms" />
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-switch
                v-model="garage"
                label="Cochera"
                color="#BAA460"
                inset
                >
                </v-switch>
              </v-col>
              <v-col>
                <v-switch
                v-model="garden"
                label="Patio"
                color="#846D34"
                inset
                >
                </v-switch>
              </v-col>
            </v-row>
            <v-row>
              <v-card-actions>
                <v-btn
                dark
                absolute
                right
                color="#BAA460"
                class="mr-4"
                @click="filterProperties"
                >Buscar
                </v-btn>
              </v-card-actions>
            </v-row>
          </v-form>
        </v-card-text>
      </v-container>
  </v-card>
</template>

<script>
import { SI_NO, HOME_TYPE } from "@/constants.js"

export default {
  name: 'searchForm',
  data() {
    return {
      amountMax: '',
      amountMin: '',
      selectedBedroom: '',
      selectedOrder: '',
      selectedPropertiType: '',
      selectedRoom: '',
      bedRooms: [1, 2, 3, 4, 5, 6, 7],
      orderBy: ["Mayor precio", "Menor precio", "Mas amplio en MTS" , "Mas chico en MTS"],
      propertiesType: HOME_TYPE,
      rooms: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      yesNoOptions: SI_NO,
      garage: null,
      garden: null,
    }
  },
  methods: {
    getQueryParams() {
      return {
        amount_max: this.amountMax,
        amount_min: this.amountMin,
        bedroom: this.selectedBedroom,
        order_by: this.selectedOrder,
        property_type: this.selectedPropertiType,
        room: this.selectedRoom,
        garage: this.garage,
        garden: this.garden,
      }
    },
    filterProperties() {
      const queryParams = this.getQueryParams();
      this.$emit('filterProperties', queryParams)
    },
    validateAmountInput() {
    }
  },
}
</script>
