<template>
  <router-link :to="{ name: 'PropertyDetail', params: { id: property.id } }">
    <div class="">
      <span>Direccion {{property.address}}</span>
      <span>Precio ${{property.price}}</span>
      <span>Descripcion: {{property.description}}</span>
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'propertyList',
  props: {
    property: Object
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
