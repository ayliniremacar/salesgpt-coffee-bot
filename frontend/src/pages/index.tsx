import React from 'react';
import Link from 'next/link';
import styles from './index.module.css';

export default function HomePage() {
  return (
    <div className={styles.container}>
      <div className={styles.hero}>
        <div className={styles.logo}>
          ☕
        </div>
        <h1 className={styles.title}>
          Premium Kahve Bot
        </h1>
        <p className={styles.description}>
          Kahve makinesi satış danışmanınız ile sohbet edin
        </p>
        <div className={styles.features}>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>💬</span>
            <span>Anlık Destek</span>
          </div>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>📋</span>
            <span>Ürün Bilgileri</span>
          </div>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>💰</span>
            <span>Fiyat Bilgileri</span>
          </div>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>📦</span>
            <span>Stok Durumu</span>
          </div>
        </div>
        <Link href="/chat" className={styles.ctaButton}>
          Sohbete Başla
        </Link>
      </div>
    </div>
  );
}