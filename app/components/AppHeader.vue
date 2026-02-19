<template>
  <header class="app-header">
    <div class="app-header__inner">
      <div class="app-header__main">
        <NuxtLink class="app-header__brand" to="/">Skillor</NuxtLink>

        <nav class="app-header__nav-links" aria-label="Primary">
          <NuxtLink to="#overview">Overview</NuxtLink>
          <NuxtLink to="#resources">Resources</NuxtLink>
          <NuxtLink to="#contact">Contact</NuxtLink>
        </nav>
      </div>

      <div class="app-header__user-links">
        <div v-if="isSignedIn" class="app-header__user-profile">
          <span class="app-header__avatar" :title="profileLabel">
            <svg
              class="app-header__avatar-icon"
              viewBox="0 0 24 24"
              role="img"
              aria-label="User"
              fill="currentColor"
            >
              <path
                d="M12 12.15a3.75 3.75 0 1 0-3.75-3.75A3.75 3.75 0 0 0 12 12.15Z"
              />
              <path
                d="M4.5 18.9a.7.7 0 0 0 .7.7h13.6a.7.7 0 0 0 .7-.7a7.5 7.5 0 0 0-15 0Z"
              />
            </svg>
            <img
              v-if="profileImageUrl"
              class="app-header__avatar-image"
              :class="{ 'is-ready': showProfileImage }"
              :src="profileImageUrl"
              alt=""
              loading="lazy"
              @error="onAvatarError"
              @load="onAvatarLoad"
            />
          </span>
          <a href="/auth/logout">Sign Out</a>
        </div>
        <NuxtLink v-else to="/auth/sign-in">Sign In</NuxtLink>
      </div>

      <button
        class="app-header__menu-button"
        :class="{ 'is-open': isMenuOpen }"
        type="button"
        aria-label="Toggle navigation"
        aria-controls="mobile-nav-links"
        :aria-expanded="isMenuOpen"
        @click="isMenuOpen = !isMenuOpen"
      >
        <span class="app-header__menu-line" />
        <span class="app-header__menu-line" />
        <span class="app-header__menu-line" />
      </button>
    </div>

    <nav
      id="mobile-nav-links"
      class="app-header__mobile-menu"
      :class="{ 'is-open': isMenuOpen }"
      aria-label="Mobile Primary"
    >
      <NuxtLink to="/" @click="closeMenu">Home</NuxtLink>
      <NuxtLink to="/#overview" @click="closeMenu">Overview</NuxtLink>
      <NuxtLink to="/#resources" @click="closeMenu">Resources</NuxtLink>
      <NuxtLink to="/#contact" @click="closeMenu">Contact</NuxtLink>
    </nav>
  </header>
</template>

<script setup lang="ts">
const isMenuOpen = ref(false);
const authUser = useUser();
const hasImageError = ref(false);
const hasImageLoaded = ref(false);

const isSignedIn = computed(() => Boolean(authUser.value));
const profileLabel = computed(
  () => authUser.value?.name || authUser.value?.email || 'User profile',
);
const profileImageUrl = computed(() => {
  const picture = authUser.value?.picture;
  if (typeof picture !== 'string') return null;
  const trimmed = picture.trim();
  return trimmed || null;
});
const showProfileImage = computed(
  () =>
    Boolean(profileImageUrl.value) &&
    hasImageLoaded.value &&
    !hasImageError.value,
);

watch(profileImageUrl, () => {
  hasImageError.value = false;
  hasImageLoaded.value = false;
});

const onAvatarLoad = () => {
  hasImageLoaded.value = true;
  hasImageError.value = false;
};

const onAvatarError = () => {
  hasImageError.value = true;
  hasImageLoaded.value = false;
};

const closeMenu = () => {
  isMenuOpen.value = false;
};
</script>

<style scoped lang="scss">
@use '../assets/scss/components/header' as *;
</style>
