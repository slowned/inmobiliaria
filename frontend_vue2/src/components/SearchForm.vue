<template>
  <v-form>
    <v-text-field v-model="amountMin" label="Precio minimo"/>
    <v-text-field v-model="amountMax" label="Precio maximo"/>
    <v-autocomplete v-model="selectedOrder" label="Ordenar Anuncios" :items="orderBy" />
    <v-autocomplete v-model="selectedRoom" label="Ambientes" :items="rooms" />
    <v-autocomplete v-model="selectedBedroom" label="Dormitorios" :items="bedRooms" />
    <v-autocomplete v-model="selectedOrder" label="Ordenar Anuncios" :items="orderBy" />
    <v-autocomplete v-model="garage" label="Cochera" :items="yesNoOptions" />
    <v-autocomplete v-model="garden" label="Patio" :items="yesNoOptions" />
    <v-select
      v-model="selectedPropertiType"
      :items="propertiesType"
      label="Tipo Inmueble"
    ></v-select>
    <v-btn
      dark
      color="#000001"
      class="mr-4"
      @click="filterProperties"
    >
      Buscar
    </v-btn>

  </v-form>
</template>

<script>
import { YES_NO, HOME_TYPE } from "@/constants.js"

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
      yesNoOptions: YES_NO,
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
