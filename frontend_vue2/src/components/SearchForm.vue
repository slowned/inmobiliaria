<template>
  <v-form>
    <v-text-field label="Precio minimo"/>
    <v-text-field label="Precio maximo"/>
    <v-autocomplete label="Inmueble" :items="propertiesType" />
    <v-btn type="submit" color="primary">Buscar</v-btn>
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
