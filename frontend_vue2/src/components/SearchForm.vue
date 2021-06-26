<template>
  <v-form color="white">
    <v-text-field label="Precio minimo"/>
    <v-text-field label="Precio maximo"/>
    <v-autocomplete label="Inmueble" :items="propertiesType" />
    <v-btn type="submit" color="#846D34">Buscar</v-btn>
  </v-form>
</template>

<script>
export default {
  name: 'searchForm',
  data() {
    return {
      propertiesType: ['Casa', 'Departamento', 'Ph'],
    }
  },
}
</script>
