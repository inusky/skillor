<template>
  <div class="default-layout">
    <AppHeader />
    <main class="default-layout__content">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import AppHeader from '../components/AppHeader.vue'
</script>

<style scoped lang="scss">
.default-layout {
  min-height: 100vh;
}

.default-layout__content {
  padding-bottom: 3rem;
}
</style>
